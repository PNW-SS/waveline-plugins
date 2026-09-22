---
name: inbox-hours
description: Configure Waveline inbox hours, lunch breaks, and public-holiday closures through the connected inbox settings tools, preserving existing schedule exceptions.
---

# Configure inbox hours and holidays

Use the Waveline integration tools for these requests. Do not switch to browser
automation or direct database writes when a connected tool lacks a capability;
explain the missing capability instead.

Identify the requested inbox with `list_inboxes`, then read `get_inbox_settings`.
Use its exact `updated_at` as `expected_updated_at` with `update_inbox_settings`.
Preserve the current timezone and open weekdays unless the user requests changes.
If first enabling a schedule, establish the timezone and all seven weekdays;
clarify unspecified weekdays when there is no existing schedule to preserve.
Lunch closures split the affected day's open intervals without opening weekends.

For standard American holidays, use `business_hours.add_holidays` with
`country: "US"`, the starting year in the inbox timezone, and `years: 15` unless
the user requests a shorter period. For one specific holiday or a selected set,
include `holiday_names` with the English calendar names, for example
`holiday_names: ["Memorial Day"]`. Omit this field only when the user requests
the full public-holiday calendar. Names match case-insensitively; unknown names
reject the entire addition and return the available names. Resolve the intended
holiday rather than dropping the filter or substituting all holidays. For a
single year's occurrence, use that year and `years: 1`.
Omit `state` for nationwide holidays. The
backend expands the public holidays using the inbox editor's calendar, including
its substitute dates. It excludes optional days and observances such as Christmas
Eve and Valentine's Day. Do not generate moving holiday dates from memory or mark
Thanksgiving as repeating on a fixed month/day. Other countries and regions may
be used when supported by the connected tool and requested by the user.

The addition is additive: existing calendar entries, custom dates, reduced
holiday hours, regular hours, and lunch breaks remain intact. Read the returned
`holiday_addition` counts and overrides before reporting success. If a preexisting
exception remains open on a requested holiday, say so rather than claiming all
holidays are closed. This operation adds dates for a bounded calendar horizon;
do not promise perpetual automatic renewal or claim it removes old calendars.

Use one operation key per authorized change and keep the same key, starting year,
and arguments on uncertain retries. On a revision conflict, read settings again
and review the newer state before a revised change. If the tool does not expose
`add_holidays` (or `holiday_names` for a selected holiday), explain that the
requested support needs a backend update and tool refresh;
plugin instructions alone cannot add a missing API capability.
