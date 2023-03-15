<div align="center">

# DiscordRainbowRole

![Alt text](https://img.shields.io/github/languages/code-size/dev-ruby/DiscordRainbowRole)
![Alt text](https://img.shields.io/github/directory-file-count/dev-ruby/DiscordRainbowRole)
![Alt text](https://img.shields.io/tokei/lines/github/dev-ruby/DiscordRainbowRole)

![Alt text](https://img.shields.io/github/issues/dev-ruby/DiscordRainbowRole)
![Alt text](https://img.shields.io/github/commit-activity/m/dev-ruby/DiscordRainbowRole)

DiscordRainbowRole은 디스코드 서버 내 역할의 색깔을 바꾸는 봇입니다.

[다운로드 1.0.0v](https://github.com/dev-ruby/DiscordRainbowRole/releases/tag/1.0.0)

</br>
</br>
</br>

# 사용법

</br>

## 1. 봇 생성

[디스코드 개발자 포탈](https://discord.com/developers/applications) 로 이동해 새 어플리케이션을 생성합니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_1.png)

</br>
</br>

앱 이름은 상관 없고, 이용약관 동의에 체크합니다
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_2.png)

</br>
</br>

어플리케이션이 만들어진 모습입니다.

좌측의 Bot 탭으로 이동합니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_3.png)

</br>
</br>

Add Bot 버튼을 눌러 봇을 생성합니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_4.png)

</br>
</br>

이곳에서 봇의 이름을 설정할 수 있습니다.

봇의 토큰을 복사해줍니다.

좌측의 OAuth2 탭으로 이동합니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_5.png)

</br>
</br>

URL Generator 탭으로 이동하고, SCOPES 탭의 bot을 체크합니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_6.png)

</br>
</br>

BOT PERMISSIONS에서 Manage Roles를 체크하고 아래의 GENERATED URL 탭에서 초대 링크를 복사하고 초대해줍니다.
![Alt text](https://raw.githubusercontent.com/dev-ruby/DiscordRainbowRole/main/res/Guide/create_discord_bot_7.png)

</br>

## 2. 역할 ID 복사하기

디스코드 내 설정 -> 고급 탭으로 이동합니다.

개발자 모드를 키면 역할에 우클릭을 할 시 `ID 복사하기` 버튼이 뜹니다.

</br>

## 3. config.json 수정

<div align="left">

```json
{
    "TOKEN" : "",
    "RoleID" : 0,
    "ChangeDelay" : 0
}
```

</div>

프로그램 폴더 내의 config.json 파일을 수정해야 합니다.

`"TOKEN" : ""`   의 "" 안에 봇의 토큰값을 넣습니다.

`"RoleID" : 0`   의 0을 역할 ID로 변경합니다.

`"ChangeDelay" : 0`   의 0을 색깔이 바뀌는데 소요될 시간으로 바꿉니다. (단위: 초)

</br>

## 4. 실행

</br>

main.exe 파일을 실행시키면 봇이 작동합니다.
