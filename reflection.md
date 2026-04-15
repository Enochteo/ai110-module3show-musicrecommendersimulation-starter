# Reflection: Pairwise Profile Output Comparisons

I compared all unique pairs of the six profiles and noted what changed in the top recommendations and why those differences make sense under the current scoring weights.

1. High-Energy Pop vs Chill Lofi: High-Energy Pop surfaces Rooftop Lights and Sunrise City, while Chill Lofi surfaces Library Rain and Midnight Coding; this makes sense because lofi targets lower energy, higher acousticness, and calmer tempos.
2. High-Energy Pop vs Deep Intense Rock: Both like high-energy tracks, but Deep Intense Rock shifts toward Storm Runner and Voltage Crown because mood/genre alignment favors intense rock over upbeat pop.
3. High-Energy Pop vs Adversarial: High Energy Sad: The adversarial profile keeps energetic songs but loses many happy/upbeat matches, so Gym Hero and Storm Runner rise while mood-consistent happy songs drop.
4. High-Energy Pop vs Adversarial: Unknown Labels: Unknown Labels moves to Dusty Highway and Velvet Lights because categorical matches are zero, so numeric closeness dominates instead of pop/happy intent.
5. High-Energy Pop vs Adversarial: Quiet Club Paradox: Quiet Club Paradox elevates Laser Bloom and Moonlit Sonata, showing conflicting targets (very low energy but euphoric/classical labels) produce unusual mixed outputs.
6. Chill Lofi vs Deep Intense Rock: Chill Lofi emphasizes low-energy, acoustic, instrumental tracks (Library Rain, Midnight Coding), while Deep Intense Rock favors high-energy and loud tracks (Storm Runner, Gym Hero).
7. Chill Lofi vs Adversarial: High Energy Sad: Chill Lofi recommendations are mellow and acoustic, while High Energy Sad pushes toward intense/high-energy songs because the energy target is high despite the sad mood label.
8. Chill Lofi vs Adversarial: Unknown Labels: Unknown Labels partially overlaps with lofi picks like Midnight Coding and Focus Flow, which makes sense because its numeric targets are mid-energy and moderate acousticness without strict label constraints.
9. Chill Lofi vs Adversarial: Quiet Club Paradox: Quiet Club Paradox keeps some calm songs but introduces Laser Bloom from mood matching, showing that a strong categorical hit can outweigh otherwise contradictory numeric preferences.
10. Deep Intense Rock vs Adversarial: High Energy Sad: These two profiles both like energetic songs, but Deep Intense Rock keeps stronger rock/intense matches while High Energy Sad allows more pop tracks due to its genre setting.
11. Deep Intense Rock vs Adversarial: Unknown Labels: Unknown Labels abandons heavy/intense tracks and centers mid-range songs because no genre/mood labels match and numeric similarity becomes the only driver.
12. Deep Intense Rock vs Adversarial: Quiet Club Paradox: Quiet Club Paradox drops most rock-heavy songs and instead mixes euphoric/classical cues with low-energy constraints, so results look less coherent than Deep Intense Rock.
13. Adversarial: High Energy Sad vs Adversarial: Unknown Labels: High Energy Sad still favors energetic songs like Gym Hero, while Unknown Labels drifts toward balanced numeric matches like Dusty Highway and Velvet Lights.
14. Adversarial: High Energy Sad vs Adversarial: Quiet Club Paradox: High Energy Sad stays consistently high-energy, while Quiet Club Paradox alternates between label matches and quiet acoustic tracks because its preferences are internally conflicting.
15. Adversarial: Unknown Labels vs Adversarial: Quiet Club Paradox: Unknown Labels yields smooth mid-profile numeric matches, while Quiet Club Paradox produces a split list where Laser Bloom and Moonlit Sonata both appear for different reasons (mood/genre vs numeric fit).
