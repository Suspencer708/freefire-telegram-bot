"""
Free Fire API Client
Handles all API calls to Free Fire data services
"""

import aiohttp
import logging
from typing import Optional, Dict, List
from config import FREEFIRE_API_KEY, FREEFIRE_API_BASE_URL

logger = logging.getLogger(__name__)


class FFAPIClient:
    """Free Fire API Client"""

    def __init__(self):
        self.api_key = FREEFIRE_API_KEY
        self.base_url = FREEFIRE_API_BASE_URL
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'FFTelegramBot/1.0'
        }

    async def get_player_stats(self, player_id: str, region: str = "pk") -> Optional[Dict]:
        """
        Get player statistics
        
        Args:
            player_id: Free Fire player UID
            region: Player region (pk, in, br, id, th, vn, etc.)
        
        Returns:
            Dictionary with player stats or None if failed
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/player/{player_id}"
                params = {'region': region}
                
                async with session.get(url, headers=self.headers, params=params) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return self._parse_stats(data)
                    else:
                        logger.error(f"API Error: {resp.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching player stats: {e}")
            return None

    async def get_player_profile(self, player_id: str, region: str = "pk") -> Optional[Dict]:
        """
        Get player profile information
        
        Args:
            player_id: Free Fire player UID
            region: Player region
        
        Returns:
            Dictionary with player profile or None if failed
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/player/{player_id}/profile"
                params = {'region': region}
                
                async with session.get(url, headers=self.headers, params=params) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return self._parse_profile(data)
                    else:
                        logger.error(f"API Error: {resp.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching player profile: {e}")
            return None

    async def get_leaderboard(self, region: str = "pk", limit: int = 10) -> Optional[List[Dict]]:
        """
        Get leaderboard for a region
        
        Args:
            region: Player region
            limit: Number of top players to fetch
        
        Returns:
            List of top players or None if failed
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/leaderboard/{region}"
                params = {'limit': limit}
                
                async with session.get(url, headers=self.headers, params=params) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return self._parse_leaderboard(data)
                    else:
                        logger.error(f"API Error: {resp.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching leaderboard: {e}")
            return None

    async def get_match_history(self, player_id: str, region: str = "pk", limit: int = 10) -> Optional[List[Dict]]:
        """
        Get player match history
        
        Args:
            player_id: Free Fire player UID
            region: Player region
            limit: Number of recent matches
        
        Returns:
            List of recent matches or None if failed
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/player/{player_id}/matches"
                params = {'region': region, 'limit': limit}
                
                async with session.get(url, headers=self.headers, params=params) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        return self._parse_matches(data)
                    else:
                        logger.error(f"API Error: {resp.status}")
                        return None
        except Exception as e:
            logger.error(f"Error fetching match history: {e}")
            return None

    def _parse_stats(self, data: Dict) -> Dict:
        """Parse raw stats data"""
        try:
            stats_data = data.get('data', {})
            return {
                'uid': stats_data.get('uid'),
                'nickname': stats_data.get('nickname'),
                'level': stats_data.get('level'),
                'rank': stats_data.get('rank'),
                'matches': stats_data.get('matches', 0),
                'wins': stats_data.get('wins', 0),
                'win_rate': round(
                    (stats_data.get('wins', 0) / stats_data.get('matches', 1)) * 100, 2
                ) if stats_data.get('matches', 0) > 0 else 0,
                'kills': stats_data.get('kills', 0),
                'kd_ratio': round(
                    stats_data.get('kills', 0) / max(stats_data.get('deaths', 1), 1), 2
                ),
                'headshots': stats_data.get('headshots', 0),
                'top10': stats_data.get('top10', 0),
                'top25': stats_data.get('top25', 0),
                'gold': stats_data.get('gold', 0),
                'diamonds': stats_data.get('diamonds', 0),
            }
        except Exception as e:
            logger.error(f"Error parsing stats: {e}")
            return {}

    def _parse_profile(self, data: Dict) -> Dict:
        """Parse raw profile data"""
        try:
            profile_data = data.get('data', {})
            return {
                'uid': profile_data.get('uid'),
                'nickname': profile_data.get('nickname'),
                'level': profile_data.get('level'),
                'rank': profile_data.get('rank'),
                'guild_name': profile_data.get('guild', {}).get('name', 'No Guild'),
                'status': profile_data.get('status', 'Offline'),
                'last_login': profile_data.get('last_login', 'N/A'),
            }
        except Exception as e:
            logger.error(f"Error parsing profile: {e}")
            return {}

    def _parse_leaderboard(self, data: Dict) -> List[Dict]:
        """Parse raw leaderboard data"""
        try:
            leaderboard = data.get('data', [])
            parsed = []
            for player in leaderboard:
                parsed.append({
                    'nickname': player.get('nickname'),
                    'uid': player.get('uid'),
                    'level': player.get('level'),
                    'rank': player.get('rank'),
                    'kd_ratio': round(
                        player.get('kills', 0) / max(player.get('deaths', 1), 1), 2
                    ),
                    'wins': player.get('wins', 0),
                })
            return parsed
        except Exception as e:
            logger.error(f"Error parsing leaderboard: {e}")
            return []

    def _parse_matches(self, data: Dict) -> List[Dict]:
        """Parse raw match history data"""
        try:
            matches = data.get('data', [])
            parsed = []
            for match in matches:
                parsed.append({
                    'match_id': match.get('match_id'),
                    'kills': match.get('kills'),
                    'placement': match.get('placement'),
                    'duration': match.get('duration'),
                    'timestamp': match.get('timestamp'),
                })
            return parsed
        except Exception as e:
            logger.error(f"Error parsing matches: {e}")
            return []
