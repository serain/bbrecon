<dl>
  <p align="center">
    <img width="320px" src="https://raw.githubusercontent.com/serain/bbrecon/master/docs/logo_cropped.png">
  </p>
  <br />
</dl>

Bug Bounty Recon (`bbrecon`) is Recon-as-a-Service for bug bounty hunters and security researchers. The API aims to provide a continuously up-to-date map of the "safe harbor" attack surface of the Internet, excluding out-of-scope targets.

The service is free.

This repository holds the CLI and Python library. Please see [the website](https://bugbountyrecon.com/) for more details.

## Important Notice

While effort is taken to ensure the results returned by `bbrecon` are reliable and trustworthy, this service and its operators are in no way responsible for what you do with the data provided.

Double check your scopes and ensure you stay within safe harbors.

## Getting Started

### API key

Fetch an API key from the Console: https://console.bugbountyrecon.com

Only Google SSO is supported at this time.

### Installation

```
$ pip3 install bbrecon

$ bbrecon configure key
Enter your API key: YOUR_API_KEY
```

## Basic Usage

Get all programs released in the last month that have "web" type targets (API, web apps etc.)

```
$ bbrecon get programs --type web --since last-month
SLUG                  PLATFORM     CREATED     REWARDS      MIN.BOUNTY    AVG.BOUNTY    MAX.BOUNTY      SCOPES  TYPES
cybrary               bugcrowd     2020-07-22  fame         $0            $0            $0                   6  android,ios,web
expressvpn            bugcrowd     2020-07-14  cash,fame    $150          $1047         $2500               17  android,ios,other,web
prestashop            yeswehack    2020-07-23  cash         $0            $0            $1000                1  web
convictional          federacy     2020-07-27  thanks       $0            $0            $0                   2  web
finra                 hackerone    2020-07-13  thanks       $0            $0            $0                   2  web
```
