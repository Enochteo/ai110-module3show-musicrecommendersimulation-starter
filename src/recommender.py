from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored: List[Tuple[float, Song]] = []
        for song in self.songs:
            score, _ = self._score_song_for_user(user, song)
            scored.append((score, song))

        scored.sort(key=lambda item: item[0], reverse=True)
        return [song for _, song in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score_song_for_user(user, song)
        if not reasons:
            return "This song has a moderate overall fit to your profile."
        return "; ".join(reasons)

    def _score_song_for_user(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons: List[str] = []

        # Experiment: half genre weight and double energy contribution.
        if song.genre.lower().strip() == user.favorite_genre.lower().strip():
            genre_points = 1.25
            score += genre_points
            reasons.append(f"genre match (+{genre_points:.1f})")

        if song.mood.lower().strip() == user.favorite_mood.lower().strip():
            mood_points = 2.5
            score += mood_points
            reasons.append(f"mood match (+{mood_points:.1f})")

        energy_diff = abs(song.energy - user.target_energy)
        energy_points = max(0.0, 6.0 * (1.0 - energy_diff))
        score += energy_points
        if energy_points >= 2.0:
            reasons.append(f"energy fit (+{energy_points:.2f})")

        acoustic_pref = 1.0 if user.likes_acoustic else 0.0
        acoustic_fit = 1.0 - abs(song.acousticness - acoustic_pref)
        acoustic_points = max(0.0, 2.0 * acoustic_fit)
        score += acoustic_points
        if acoustic_points >= 1.5:
            reasons.append(f"acoustic preference fit (+{acoustic_points:.2f})")

        return score, reasons

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    numeric_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
        "speechiness",
        "instrumentalness",
        "liveness",
        "loudness_db",
    }

    with open(csv_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            parsed: Dict = {}
            for key, value in row.items():
                if key == "id":
                    parsed[key] = int(value)
                elif key in numeric_fields:
                    parsed[key] = float(value)
                else:
                    parsed[key] = value
            songs.append(parsed)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    # Point strategy (experiment):
    # - Genre gets 1.25 points (half weight), Mood gets 2.5 points
    # - Numeric similarity contributes up to 5.0 points total
    if song["genre"].lower().strip() == user_prefs["favorite_genre"].lower().strip():
        genre_points = 1.25
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    if song["mood"].lower().strip() == user_prefs["favorite_mood"].lower().strip():
        mood_points = 2.5
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    # Stronger numeric signals in this catalog.
    numeric_weights = {
        "energy": 2.4,
        "tempo_bpm": 1.0,
        "valence": 0.9,
        "danceability": 0.8,
        "acousticness": 0.4,
        "speechiness": 0.2,
        "instrumentalness": 0.2,
        "liveness": 0.1,
        "loudness_db": 0.2,
    }

    # Normalization ranges chosen from dataset scale conventions.
    feature_ranges = {
        "energy": 1.0,
        "tempo_bpm": 120.0,
        "valence": 1.0,
        "danceability": 1.0,
        "acousticness": 1.0,
        "speechiness": 1.0,
        "instrumentalness": 1.0,
        "liveness": 1.0,
        "loudness_db": 30.0,
    }

    numeric_raw = 0.0
    numeric_max = sum(numeric_weights.values())
    for feature, weight in numeric_weights.items():
        target_key = f"target_{feature}"
        if target_key not in user_prefs or feature not in song:
            continue

        diff = abs(song[feature] - user_prefs[target_key])
        similarity = max(0.0, 1.0 - (diff / feature_ranges[feature]))
        numeric_raw += weight * similarity

    if numeric_max > 0:
        numeric_points = (numeric_raw / numeric_max) * 5.0
        score += numeric_points
        if numeric_points >= 3.0:
            reasons.append(f"audio-feature fit (+{numeric_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "overall profile similarity"
        scored.append((song, score, explanation))

    scored.sort(key=lambda row: row[1], reverse=True)
    return scored[:k]
