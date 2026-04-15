"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs

MAX_FUNCTIONAL_SCORE = 8.75


USER_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "indie pop",
        "favorite_mood": "happy",
        "target_energy": 0.82,
        "target_tempo_bpm": 126.0,
        "target_valence": 0.85,
        "target_danceability": 0.84,
        "target_acousticness": 0.20,
        "target_speechiness": 0.08,
        "target_instrumentalness": 0.05,
        "target_liveness": 0.15,
        "target_loudness_db": -6.0,
        # Compatibility keys for starter scoring logic.
        "genre": "indie pop",
        "mood": "happy",
        "energy": 0.82,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.36,
        "target_tempo_bpm": 76.0,
        "target_valence": 0.60,
        "target_danceability": 0.58,
        "target_acousticness": 0.84,
        "target_speechiness": 0.04,
        "target_instrumentalness": 0.72,
        "target_liveness": 0.09,
        "target_loudness_db": -15.5,
        # Compatibility keys for starter scoring logic.
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.36,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "target_tempo_bpm": 154.0,
        "target_valence": 0.45,
        "target_danceability": 0.62,
        "target_acousticness": 0.08,
        "target_speechiness": 0.06,
        "target_instrumentalness": 0.02,
        "target_liveness": 0.18,
        "target_loudness_db": -4.5,
        # Compatibility keys for starter scoring logic.
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
    },
}

EDGE_CASE_PROFILES = {
    # Conflicting affect profile: very high energy but low-valence mood target.
    "Adversarial: High Energy Sad": {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.90,
        "target_tempo_bpm": 140.0,
        "target_valence": 0.20,
        "target_danceability": 0.55,
        "target_acousticness": 0.15,
        "target_speechiness": 0.06,
        "target_instrumentalness": 0.02,
        "target_liveness": 0.12,
        "target_loudness_db": -5.0,
        # Compatibility keys for starter scoring logic.
        "genre": "pop",
        "mood": "sad",
        "energy": 0.90,
    },
    # Non-existent labels test: categorical matches should fail and rely on numeric fit.
    "Adversarial: Unknown Labels": {
        "favorite_genre": "hyperfolkcore",
        "favorite_mood": "astral",
        "target_energy": 0.52,
        "target_tempo_bpm": 105.0,
        "target_valence": 0.58,
        "target_danceability": 0.61,
        "target_acousticness": 0.41,
        "target_speechiness": 0.07,
        "target_instrumentalness": 0.19,
        "target_liveness": 0.11,
        "target_loudness_db": -10.0,
        # Compatibility keys for starter scoring logic.
        "genre": "hyperfolkcore",
        "mood": "astral",
        "energy": 0.52,
    },
    # Extreme mismatch pressure test: near-silent + very high danceability request.
    "Adversarial: Quiet Club Paradox": {
        "favorite_genre": "classical",
        "favorite_mood": "euphoric",
        "target_energy": 0.05,
        "target_tempo_bpm": 170.0,
        "target_valence": 0.95,
        "target_danceability": 0.95,
        "target_acousticness": 0.98,
        "target_speechiness": 0.01,
        "target_instrumentalness": 0.95,
        "target_liveness": 0.02,
        "target_loudness_db": -22.0,
        # Compatibility keys for starter scoring logic.
        "genre": "classical",
        "mood": "euphoric",
        "energy": 0.05,
    },
}

ALL_PROFILES = {**USER_PROFILES, **EDGE_CASE_PROFILES}

def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, profile_prefs in ALL_PROFILES.items():
        recommendations = recommend_songs(profile_prefs.copy(), songs, k=5)

        print(f"\nProfile: {profile_name}")
        print("Top Recommendations")
        print("=" * 72)
        for idx, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            reasons = [r.strip() for r in explanation.split(",") if r.strip()]

            print(f"{idx}. {song['title']}")
            print(f"   Final Score : {score:.2f} / {MAX_FUNCTIONAL_SCORE:.2f}")
            print("   Reasons     :")
            if reasons:
                for reason in reasons:
                    print(f"     - {reason}")
            else:
                print("     - overall profile similarity")
            print("-" * 72)


if __name__ == "__main__":
    main()
