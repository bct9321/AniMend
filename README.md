# AniMend
AniMend is an AI-powered tool that harmonizes your anime directory structures. It identifies anime titles in English and Japanese and fetches corresponding AniDB IDs, simplifying your anime organization process and enhancing your viewing experience.

## Example
Consider the following directory structure:


```shell
D:/anime
D:/anime/Shinsekai Yori
D:/anime/Cowboy Beebop
```
With correctly functioning send_to_chat_gpt_batch and fetch_anidb_id_batch methods, we can anticipate the following outputs:

### Shinsekai Yori
- English translation: "From the New World"
- Japanese: "新世界より"
- AniDB ID: 9002
### Cowboy Beebop
- English translation: "Cowboy Bebop" (the name is already in English)
- Japanese: "カウボーイビバップ"
- AniDB ID: 23
This leads to the expected output:

```shell
Original Name: Shinsekai Yori
Formatted Name: Shinsekai Yori (From the New World, 新世界より) [anidb=9002]

Original Name: Cowboy Beebop
Formatted Name: Cowboy Beebop (Cowboy Bebop, カウボーイビバップ) [anidb=23]
```
Please note that the provided AniDB IDs for these shows are placeholders, and actual results may vary.
