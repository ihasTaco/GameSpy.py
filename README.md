# Python-GameSpy
A simple script to query GameSpy 1 servers made in python<br>
This will eventually be used as a Query Module for [ServerQuery](https://github.com/ihasTaco/ServerQuery)

# Coming Soon
 - Readme
 - an actual script
 - documentation
 - GameSpy v2 & v3

# Supported Games
Unfortunately, there isn't a centralized repository containing a comprehensive list of games that were supported by GameSpy. Furthermore, with the closure of GameSpy, the majority of games have transitioned away from using it. Nonetheless, I have diligently included as many games as possible that have utilized GameSpy at some stage in their lifespan. However, if further investigation reveals that a particular game has migrated to a protocol completely unrelated to GameSpy v1, v2, or v3, it may be removed from the "Supported Games" list or relocated to a different section.

Please note that this list is not exhaustive, and some of the items mentioned may not utilize GameSpy v1 at all. Instead, they might use GameSpy v2 or v3, or moved to a different protocol entirely.

To ensure the accuracy of this list, I have personally gone through each entry and attempted to find public servers. I have also made an effort to verify if the servers were queryable. However, it was a challenging task as finding query ports for certain games proved difficult, and some servers even change their query ports. Which means that until I have the time and resources to set up a dedicated server for thoroughly building and testing each game server, this list may remain incomplete.

I understand that this limitation might be disappointing to some users, and I apologize for any inconvenience caused. However, I will continue to update the list regularly as new information becomes available, and I encourage the community to contribute by testing and adding any servers that have not been included.

Therefore, it is possible that some games on this list, which have not been tested, may no longer function with GameSpy v1.

If you own or are aware of a server that has not been tested, I kindly request you to try out the script and update the list of supported games. Your contribution would be greatly appreciated!

*NOTE:* The script does allow users to query the Rules of the server but, at least with the servers I was able to test, just sent back the server info, so the column has been excluded from this list

|                  Game                                 |                    App ID                     |     API     |       Tested       |    Server Info     |    Player Info     |       Notes        |
|-------------------------------------------------------|:---------------------------------------------:|:-----------:|:------------------:|:------------------:|:------------------:|:------------------:|
| Aliens versus Predator 2                              | [3730](https://steamdb.info/app/3730)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Arma: Cold War Assault                                | [65790](https://steamdb.info/app/65790)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Arma: Armed Assault                                   | [65780](https://steamdb.info/app/65780)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Arma 2                                                | [33900](https://steamdb.info/app/33900)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Area 51 (2005)                                        | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Battlefield 1942                                      | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Battlefield 2                                         | [--](##)                                      | GameSpy v3  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Battlefield 2142                                      | [--](##)                                      | GameSpy v2 or v3  | :x:          | :heavy_minus_sign: | :heavy_minus_sign: |
| Battlefield Vietnam                                   | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Blitzkrieg Anthology                                  | [313480](https://steamdb.info/app/313480)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Command & Conquer 3: Tiberium Wars                    | [24790](https://steamdb.info/app/24790)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Command & Conquer 3: Kane's Wrath                     | [24810](https://steamdb.info/app/24810)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Command & Conquer: Generals                           | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Command & Conquer: Renegade                           | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Crysis                                                | [17300](https://steamdb.info/app/17300)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Crysis: Warhead                                       | [17330](https://steamdb.info/app/17330)       | GameSpy v1  | :white_check_mark: | :heavy_minus_sign: | :heavy_minus_sign: | Port 27900 just gives "status: none"
| Daikatana                                             | [242980](https://steamdb.info/app/242980)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Dungeon Lords: Steam Edition                          | [271760](https://steamdb.info/app/271760)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Empire Earth II                                       | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Halo: Combat Evolved                                  | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: | 
| James Bond: Nightfire                                 | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Land of the Dead: Road to Fiddler's Green             | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| The Lord of the Rings: The Battle for Middle-earth    | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| The Lord of the Rings: The Battle for Middle-earth II | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Majesty: Gold HD                                      | [25990](https://steamdb.info/app/25990)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Medal of Honor: Allied Assualt                        | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Medal of Honor: Breakthrough                          | [--](##)                                      | GameSpy v1  | :white_check_mark: | :heavy_minus_sign: | :heavy_minus_sign: | Not sure if not supported or just couldn't find the query port
| Medal of Honor: Spearhead                             | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Medieval II: Total War                                | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Microsoft Flight Simulator X: Steam Edition           | [314160](https://steamdb.info/app/314160)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Moonbase Commander                                    | [254880](https://steamdb.info/app/254880)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Neverwinter Nights                                    | [704450](https://steamdb.info/app/704450)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Neverwinter Nights 2                                  | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| No One Lives Forever 2: A Spy in H.A.R.M.'s Way       | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| The Operative: No One Lives Forever                   | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Railroad Tycoon 3                                     | [7610](https://steamdb.info/app/7610)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Rise of Nations: Extended Edition                     | [287450](https://steamdb.info/app/287450)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Rome: Total War                                       | [885970](https://steamdb.info/app/885970)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Rune                                                  | [210950](https://steamdb.info/app/210950)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Serious Sam: The First Encounter                      | [41050](https://steamdb.info/app/41050)       | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Serious Sam: The Second Encounter                     | [41060](https://steamdb.info/app/41060)       | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Serious Sam 2                                         | [204340](https://steamdb.info/app/204340)     | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Sid Meier's Civilization III: Complete                | [3910](https://steamdb.info/app/3910)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Sid Meier's Civilization IV                           | [3900](https://steamdb.info/app/3900)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Sid Meier's Civilization IV: Colonization             | [16810](https://steamdb.info/app/16810)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Soldier of Fortune                                    | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Soldier of Fortune II: Double Helix                   | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| S.T.A.L.K.E.R.: Shadow of Chernobyl                   | [4500](https://steamdb.info/app/4500)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| S.T.A.L.K.E.R.: Clear Sky                             | [20510](https://steamdb.info/app/20510)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| S.T.A.L.K.E.R.: Call of Pripyat                       | [41700](https://steamdb.info/app/41700)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Star Wars: Battlefront                                | [1237980](https://steamdb.info/app/1237980)   | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Star Wars: Battlefront II                             | [1237950](https://steamdb.info/app/1237950)   | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Star Trek: Elite Force II                             | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Star Wars: Empire at War - Gold Pack                  | [32470](https://steamdb.info/app/32470)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Star Trek: Starfleet Command II - Empires at War      | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Star Trek: Starfleet Command III                      | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Stronghold 2: Steam Edition                           | [40960](https://steamdb.info/app/40960)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Stronghold Legends: Steam Edition                     | [40980](https://steamdb.info/app/40980)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| SWAT 4                                                | [--](##)                                      | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Test Drive Unlimited                                  | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Tribes 2                                              | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Tribes: Vengeance                                     | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Unreal                                                | [--](##)                                      | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Unreal Tournament (1999)                              | [13240](https://steamdb.info/app/13240)       | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Unreal Tournament (2004)                              | [13230](https://steamdb.info/app/13230)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Unreal Tournament 3                                   | [13210](https://steamdb.info/app/13210)       | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Vietcong                                              | [860190](https://steamdb.info/app/860190)     | GameSpy v1  | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Warhammer 40,000: Dawn of War                         | [4570](https://steamdb.info/app/4570)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Warhammer 40,000: Winter Assault                      | [9310](https://steamdb.info/app/9310)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Warhammer 40,000: Dark Crusade                        | [4580](https://steamdb.info/app/4580)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
| Warhammer 40,000: Soulstorm                           | [9450](https://steamdb.info/app/9450)         | GameSpy v1  | :x:                | :heavy_minus_sign: | :heavy_minus_sign: |
