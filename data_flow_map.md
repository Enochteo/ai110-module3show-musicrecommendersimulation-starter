# Music Recommender Data Flow Map

## 1) Input: User Preferences

The system starts with a user profile dictionary from src/main.py.

Example fields used:

- favorite_genre
- favorite_mood
- target_energy
- target_tempo_bpm
- target_valence
- target_danceability
- target_acousticness
- target_speechiness
- target_instrumentalness
- target_liveness
- target_loudness_db

At the same time, songs are loaded from data/songs.csv using load_songs().

## 2) Process: Score Every Song (The Loop)

Core loop inside recommend_songs():

1. For each song in songs:
2. Call score_song(user_prefs, song)
3. Compute a total score out of 10:
   - Genre match: +2.5 points
   - Mood match: +2.5 points
   - Numeric audio similarity: up to +5.0 points total
4. Collect reason strings (for explanation text)
5. Store tuple: (song, score, explanation)

Mental model:
Input prefs + one song -> scoring rules -> one scored result
(repeated for every song in the CSV)

## 3) Output: Rank and Return Top K

After all songs are scored:

1. Sort all scored tuples by score descending
2. Slice first k results
3. Return top k recommendations as:
   (song_dict, score, explanation)

Final pipeline summary:
User Prefs + Songs CSV -> per-song scoring loop -> sorted ranking -> Top K recommendations

## 4) Mermaid Flowchart

```mermaid
flowchart TD
   A[Input: User Preferences] --> C[recommend_songs]
   B[Input: Songs CSV] --> D[load_songs]
   D --> C

   C --> E{For each song}
   E --> F[score_song(user_prefs, song)]
   F --> G[Build tuple: song, score, explanation]
   G --> E
   E --> H[All songs scored]

   H --> I[Sort by score descending]
   I --> J[Take Top K]
   J --> K[Output: Top K Recommendations]
```
