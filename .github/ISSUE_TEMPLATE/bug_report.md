name: 🐛 Bug Report
description: Report a bug or issue with the application
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!

  - type: dropdown
    id: version
    attributes:
      label: Version
      description: What version are you using?
      options:
        - v1.0.0 (.exe)
        - Running from source
    validations:
      required: true

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Describe the issue clearly
      placeholder: Tell us what you expected to happen and what actually happened
    validations:
      required: true

  - type: textarea
    id: steps
    attributes:
      label: Steps to Reproduce
      description: How can we reproduce this issue?
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. See error
    validations:
      required: true

  - type: textarea
    id: logs
    attributes:
      label: Relevant Log Output
      description: Copy and paste any relevant log output
      render: shell

  - type: dropdown
    id: os
    attributes:
      label: Operating System
      options:
        - Windows 10
        - Windows 11
    validations:
      required: true

  - type: textarea
    id: lm-studio
    attributes:
      label: LM Studio Setup
      description: What model are you using in LM Studio?
      placeholder: Model name and version if known
