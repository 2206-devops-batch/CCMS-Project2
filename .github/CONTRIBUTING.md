# **Contributing.md** needs to be updated by the **`YOUR-ORGANIZATION`**

## How To Contribute

You can contribute to YOUR-REPO in various ways, including:

- [Reporting bugs or issues][reporting-issues] on GitHub. \
- Looking at existing [issues] and adding more information, particularly helping to reproduce the issues.
  > Please make sure to include/fill in all the details in the issue template to make sure the issue can be addressed as quickly as possible.
- [Submitting a pull request]([contributing-guide]#submitting-a-pull-request) with a bug fix or an improvement.
- Helping other people on the [Github Discussions][discussions].

<!-- - [Submitting improvements to the documentation][wiki]. Updates, enhancements, new guides, spelling fixes... -->

---

## Please read [Steps to Contribute][steps-to-contribute] & [Understanding What Makes A Good Commit Message][understanding-good-commit-message]

### Setting up the repository for development

1. Fork the [Repository][repo].
2. Clone the **Forked** Repository and create a feature branch.
   (Existing contributors can create feature branches without forking. Prefix the branch name with `@your-github-username/`.)
3. You can then run `YOUR-STARTING-COMMAND` in the root folder to get started.

### Branching

**The `main` branch of this repository should be kept releasable at any/all times.** \
This way we can continuously deploy (CD) fixes and improvements without costly \
managing of different branches and issues will be noticed and fixed quickly. \
This also ensures other contributors can check out the latest version from \
GitHub and work on it with minimal disruption from other features in progress.

Keeping the `main` releasable means that changes merged to it need to be:

- **Backwards compatible**: If the code you're adding depends on a feature only present in newer or unreleased SDK versions, it needs to check which SDK version is being used and not assume the latest version is being used.
- **Non-breaking**: If code that is unreleasable or fails the test suite ends up in main, it should be reverted.
- **Tested**: Always include a test plan in pull requests. Do not merge code that doesn't pass all automated tests.

<!--
## Available Scripts

### Learn More

## :rocket: Deployment
-->

### Submitting a pull request

To submit a pull request:

1. Write the description of your pull request. Make sure to include a test plan and test your changes.
2. Make sure all tests pass on -TESTING PLATFORM-. <!-- CircleCI. -->
3. Wait for a review and adjust the code if necessary.

<!-- Definitions/Links -->

<!-- External Based -->

[cs]: https://codesandbox.io
[rubberduck]: https://rubberduckdebugging.com
[understanding-good-commit-message]: https://chris.beams.io/posts/git-commit
[xy]: https://meta.stackexchange.com/questions/66377/what-is-the-xy-problem/66378#66378
[minimal, reproducible example]: https://stackoverflow.com/help/minimal-reproducible-example
[steps-to-contribute]: https://www.dataschool.io/how-to-contribute-on-github/#gettingstarted

<!-- Repo Based -->

[author]: https://YOUR-Domain.com
[repo]: https://github.com/YOUR-ORGANIZATION/YOUR-REPO

[wiki]: [repo]/wiki
[discussions]: [repo]/discussions
[curr-branch]: [repo]/blob/main
[.github]: [curr-branch]/.github

[license]: [.github]/LICENSE
[support-docs]: [.github]/Support.md
[code-of-conduct]: [.github]/Code-of-conduct.md
[contributing-guide]: [.github]/Contributing.md

<!-- [ideas]: https://github.com/YOUR-ORGANIZATION/ideas -->

[search-github-issues]: https://github.com/type=Issues&search?q=user%3AYOUR-ORGANIZATION
[issues]: https://github.com/YOUR-ORGANIZATION/YOUR-REPO/issues
[reporting-issues]: [issues]/new

<!-- Definitions/Links END -->
