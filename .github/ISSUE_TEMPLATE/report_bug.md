name: Report a bug
about: Report a bug in Afrodita.
labels: 'bug: unconfirmed'
inputs:
- type: description
  attributes:
    value: |
      Thanks for taking the time to report an EssentialsX bug! Fill out the form below to provide us with info to help fix the bug.
      Only use this if you're 100% sure you've found a bug and can reproduce it. If you're looking for general help with EssentialsX, try the Q&A forum or MOSS Discord server.
- type: multi_select
  attributes:
    label: Type of bug
    description: What type of bug is this? Choose all that apply.
    required: true
    choices:
      - Bug
      - Improvement
      - Taks
    validations:
      required: false
- type: textarea
  attributes:
    label: Bug description
    description: Describe roughly what the bug is here.
    required: true
    placeholder: |
      Example: "When running /nuke after putting everyone into adventure mode, there aren't any explosions..."
- type: textarea
  attributes:
    label: Steps to reproduce
    description: Provide an example of how to trigger the bug.
    required: true
    Value: |
      Steps:
      1. 
      2. 
      3. 
- type: textarea
  attributes:
    label: Expected behaviour
    description: Explain what you should expect to happen.
    required: true
    placeholder: |
      Example: "Everything should explode!"
    validations:
      required: true    
      
- type: textarea
  attributes:
    label: Actual behaviour
    description: Explain what actually happens.
    required: true
    placeholder: |
      Example: "Everything doesn't explode :("
    validations:
      required: true