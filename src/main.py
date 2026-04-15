"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


TASTE_PROFILE = {
    "favorite_genre": "indie pop",
    "favorite_mood": "happy",
    "target_energy": 0.78,
    "target_tempo_bpm": 122.0,
    "target_valence": 0.82,
    "target_danceability": 0.80,
    "target_acousticness": 0.30,
    "target_speechiness": 0.07,
    "target_instrumentalness": 0.06,
    "target_liveness": 0.13,
    "target_loudness_db": -7.0,
    # Compatibility keys for starter scoring logic.
    "genre": "indie pop",
    "mood": "happy",
    "energy": 0.78,
}


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Concrete taste profile for recommendation comparisons.
    user_prefs = TASTE_PROFILE.copy()

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 72)
    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        reasons = [r.strip() for r in explanation.split(",") if r.strip()]

        print(f"{idx}. {song['title']}")
        print(f"   Final Score : {score:.2f} / 10.00")
        print("   Reasons     :")
        if reasons:
            for reason in reasons:
                print(f"     - {reason}")
        else:
            print("     - overall profile similarity")
        print("-" * 72)


if __name__ == "__main__":
    main()
