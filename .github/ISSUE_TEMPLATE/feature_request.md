name: 💡 Feature Request
description: Suggest an idea or feature for the application
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a feature!

  - type: textarea
    id: problem
    attributes:
      label: Is your feature request related to a problem?
      description: Describe what the problem is
      placeholder: A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

  - type: textarea
    id: solution
    attributes:
      label: Describe the solution you'd like
      description: What do you want to happen?
      placeholder: A clear and concise description of what you want to happen
    validations:
      required: true

  - type: textarea
    id: alternatives
    attributes:
      label: Describe alternatives you've considered
      description: Any alternative solutions or features you've considered?
      placeholder: A clear and concise description of any alternative solutions or features you've considered

  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - Nice to have
        - Important
        - Critical
    validations:
      required: true

  - type: textarea
    id: additional
    attributes:
      label: Additional Context
      description: Add any other context, screenshots, or examples about the feature request here
