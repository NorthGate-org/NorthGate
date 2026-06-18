# Contributing

Thank you for your interest in contributing to NorthGate. This document explains the expected contribution process and the minimum requirements for submitting changes to the project.

## Contribution workflow

1. Fork the project repository.
2. Create a new branch in your fork for the change you want to make.
3. Make your changes in a focused and maintainable way.
4. Add or update unit tests for all new features and behavior changes.
5. Document the process followed and the results of your changes.
6. Open a pull request from your fork into the main project repository.

## Pull request requirements

All contributions must be submitted through a pull request.

Each pull request must:

- Clearly describe the purpose of the change.
- Explain the process used to implement the change.
- Include the results of testing or validation.
- Include unit tests for every new feature.
- Keep unrelated changes out of the pull request.
- Be reviewed and approved by the project admin and maintainer before it can be merged.

Pull requests that do not include the required tests or documentation may be delayed until the missing information is added.

## Unit tests

All new features must include unit tests.

Tests should verify the expected behavior of the feature and cover important edge cases where appropriate. If an existing feature is changed, update the related tests so they continue to describe the intended behavior of the project.

Before submitting a pull request, run the available test suite and include the results in the pull request description.

## Documentation

Contributors are expected to document both the process and the results of their work.

Documentation should include:

- What was changed.
- Why the change was made.
- How the change was implemented.
- How the change was tested.
- Any limitations, known issues, or follow-up work.

Documentation may be added to project files when the change affects user behavior, developer setup, architecture, configuration, or supported workflows. For smaller changes, the pull request description may be enough if it clearly explains the process and results.

## Review and merge policy

The project admin and maintainer are responsible for reviewing pull requests.

A pull request must not be merged until it has been reviewed and approved by the admin and maintainer. Review may include checking code quality, project scope, test coverage, documentation, security impact, and compatibility with the goals of NorthGate.

## Code quality expectations

Contributions should be clear, focused, and consistent with the existing project style.

Please avoid unnecessary refactoring, unrelated formatting changes, or large changes that combine multiple independent goals. Smaller pull requests are easier to review and maintain.

