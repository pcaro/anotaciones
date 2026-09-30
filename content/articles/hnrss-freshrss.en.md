Title: hnrss: custom RSS feeds for Hacker News
Date: 2026-09-28
Tags: rss, hackernews, freshrss, nas, self-hosted, feeds
Slug: hnrss-freshrss
Lang: en
Featured_image: /images/hnrss-freshrss.png
Summary: hnrss.org generates custom RSS, Atom and JSON feeds for Hacker News. I use it to follow only what matters to me from my self-hosted FreshRSS on the NAS.
Category: Herramientas

![hnrss and FreshRSS on the NAS](/images/hnrss-freshrss.png)

[Hacker News](https://news.ycombinator.com/) has no RSS. Or rather, it doesn't have the RSS I'd want: a single front-page feed with no filters or searches. Luckily there's [hnrss.org](https://hnrss.github.io/), which generates custom, real-time feeds from the site and Algolia's search API.

## What hnrss.org is

It's a service (with [open source](https://github.com/hnrss/hnrss)) that exposes dozens of endpoints. You build the URL around whatever you want to follow and get valid RSS over HTTPS. The main feed types:

**Firehose**: everything new, posts and comments.

```text
https://hnrss.org/newest
https://hnrss.org/newcomments
https://hnrss.org/frontpage
```

**Searches**: posts or comments containing a keyword.

```text
https://hnrss.org/newest?q=rust
https://hnrss.org/newcomments?q=kubernetes
```

You can combine terms with `OR` and percent-encode reserved characters (e.g. `C%2B%2B`).

**Replies**: comments replying to a user or a specific comment.

```text
https://hnrss.org/replies?id=USERNAME
https://hnrss.org/replies?id=17752464
```

**Points and activity**: only items above a threshold.

```text
https://hnrss.org/newest?points=300
https://hnrss.org/newest?comments=250
```

**Self-posts**: Ask HN, Show HN and polls.

```text
https://hnrss.org/ask
https://hnrss.org/show
https://hnrss.org/polls
```

**Jobs**: YC startup openings and the monthly "Who is hiring?" threads.

**Users**: what a given person posts or comments.

Besides RSS, any endpoint accepts `.atom` or `.jsonfeed` at the end:

```text
https://hnrss.org/frontpage.atom
https://hnrss.org/ask.jsonfeed?comments=10
```

## Parameters I use

The ones I get the most out of:

- `points=N` and `comments=N` to filter firehose noise. It's the quickest way to turn down the volume on `newest`.
- `q=...` to watch specific topics without opening a browser.
- `count=N` to get more than the default 20 items (hard limit of 100).
- `link=comments` so the item link points to the HN thread instead of the original article.
- `description=0` if you only want links, with no description.

```text
https://hnrss.org/newest?q=linux&points=100&count=50
```

## How I use it in my NAS FreshRSS

I run [FreshRSS](https://freshrss.org/) in Docker on the NAS, which is my central feed reader. Adding an hnrss feed works like any other: in the web UI, **Subscription → Add a feed**, paste the URL, done.

What I have set up:

- The front page (`/frontpage`) for the daily pulse.
- A couple of per-topic searches (`?q=python`, `?q=postgres`) with a minimum `points`, which is where saving time really pays off.
- The "Who is hiring?" threads filtered with `q=` whenever I feel like checking the market.

Since FreshRSS fetches on a schedule, it's worth tuning the frequency. The hnrss docs ask you to be especially conservative with the endpoints that scrape HN (e.g. `/favorites`), so a long interval is better there. For the rest, updating every 30-60 minutes is plenty: HN isn't going anywhere in that time.

The advantage of having it all in FreshRSS is obvious: a single place where I read, star and search, with my own filtering rules, and without depending on the HN front page or its ranking.

*Source*: [Hacker News RSS](https://hnrss.github.io/)
