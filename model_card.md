# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This model recommends songs from a small catalog.
It uses a user taste profile to pick top matches.
It assumes users can describe their genre, mood, and audio preferences.
This project is for classroom learning, not production use.

---

## 3. How the Model Works

Each song has features like genre, mood, energy, tempo, valence, and danceability.
Each user profile has target values for those features.
The model gives points for genre and mood matches.
It also adds numeric similarity points for audio features.
Songs are sorted by total score, and the top K are returned.
In my experiment, I reduced genre weight and increased energy weight.

---

## 4. Data

The dataset has 20 songs.
It includes many genres, like pop, lofi, rock, classical, metal, and latin.
It includes many moods, like happy, chill, intense, euphoric, and calm.
I did not add or remove songs.
The data is still small and cannot represent all music tastes.

---

## 5. Strengths

It works well for users with clear and consistent preferences.
The top songs usually match the expected vibe for standard profiles.
The reason strings make the recommendations easy to understand.
The model is simple, transparent, and easy to debug.

---

## 6. Limitations and Bias

This model can create a filter bubble.
If a user enters a genre or mood not in the dataset, category matches become zero.
Then numeric similarity dominates, and energy has the biggest effect because its weight is highest.
That can push users toward the same energy band, even when their intent is different.
Users with rare labels may get weaker recommendations than users with common labels.

---

## 7. Evaluation

I tested six profiles.
Three were standard profiles, and three were adversarial profiles.
I checked if top songs matched each profile's intended vibe.
I also checked if reasons and point values matched the scoring logic.
The biggest surprise was that Unknown Labels still gave confident rankings from numeric features alone.
I also ran pytest to make sure core behavior still passed tests.

---

## 8. Future Work

I would add fuzzy matching for genre and mood labels.
I would add a diversity rule so top results are less repetitive.
I would let users set multiple moods or mixed preferences.
I would compare results before and after weight changes automatically.
I would test with a larger and more balanced dataset.

---

## 9. Personal Reflection

My biggest learning moment was seeing how one small weight change could reorder many top results.
AI tools helped me move faster when drafting scoring logic, testing profile ideas, and generating explanations.
I still had to double-check the AI output by running experiments, checking score math, and confirming that reasons matched the actual points.
I was surprised that a simple weighted score still felt like a real recommendation system when the outputs matched a user's vibe.
I was also surprised that it could look confident even when labels did not match the dataset.
If I extend this project, I would add fuzzy label matching, diversity constraints, and a larger dataset to reduce bias and repetition.
