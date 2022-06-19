# Github Activity Summaries

[![Actions Status](https://github.com/ietf-github-services/activity-summary/workflows/Activity%20Summary/badge.svg)](https://github.com/ietf-github-services/activity-summary/actions)

This repo e-mails weekly summaries of GitHub repository activity to IETF mailing lists.

You can get a summary of repository activity e-mailed by creating a pull request that updates `mls.json` in this repository, with a new member of the top-level object representing the mailing list you'd like to send the summary to. 

For example:

~~~
"quic@ietf.org": {                         <-- your group's e-mail address
    "digest:sunday": {                     <-- must be "digest:sunday"
        "eventFilter": {                   <-- optional section to filter the issue labels
            "notlabel": [
                "editorial"
            ]
        },
        "repos": [                         <-- list of repos to watch
            "quicwg/base-drafts"
        ],
        "topic": "QUIC Activity Summary"   <-- subject for the summary
    }
}
~~~

Activity summaries will be e-mailed weekly.
