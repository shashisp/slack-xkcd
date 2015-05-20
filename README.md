# slack-xkcd

## Usage

From any Slack channel, just type `/xkcd`. random xkcd comics will be shown on the same channel visible just to you.

## Integrate with your team

1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
  - Command: `/ipl`
  - URL: `http://slack-xkcd.herokuapp.com`
  - Method: `GET`
  - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Stop Juggling between tabs, web comics now in Slack.`
