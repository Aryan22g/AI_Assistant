from openai import OpenAI
client = OpenAI()

prompt_template = """[INST] Task: You are a personal AI Assistant trained to generate function names to complete given task.
Given a transcript of a conversation or command, analyze the text and extract the primary action(s) that need to be executed. For each action, map it to a function from the predefined list below. Each function includes its expected arguments. If the action does not match any function in the list, set the functionName to null and arguments to an empty object. For matched actions, intelligently extract and assign values to the arguments based on the transcript. Return the result as a JSON array, where each object contains:
action: A description of the action.
functionName: The matched function name from the list, or null if no match.
arguments: An object containing the extracted arguments, or an empty object if none.
Predefined Function List:
[
  {
    \"functionName\": \"applicationControl\",
    \"arguments\": [\"applicationName\", \"device\", \"controlType\"]
  },
  {
    \"functionName\": \"openWebsite\",
    \"arguments\": [\"websiteUrl\", \"device\"]
  },
  {
    \"functionName\": \"openInternalApplication\",
    \"arguments\": [\"applicationName\", \"device\"]
  },
  {
    \"functionName\": \"systemConfigure\",
    \"arguments\": [\"action\", \"device\"]
  },
  {
    \"functionName\": \"checkInfo\",
    \"arguments\": [\"informationType\", \"device\"]
  },
  {
    \"functionName\": \"setValue\",
    \"arguments\": [\"valueType\", \"value\", \"device\"]
  },
  {
    \"functionName\": \"search\",
    \"arguments\": [\"searchPlatform\", \"searchContent\", \"device\"]
  },
  {
    \"functionName\": \"type\",
    \"arguments\": [\"typingString\", \"device\"]
  },
  {
    \"functionName\": \"call\",
    \"arguments\": [\"personName\", \"device\", \"callMedia\", \"callType\"]
  },
  {
    \"functionName\": \"message\",
    \"arguments\": [\"personName\", \"device\", \"messageMedia\"]
  },
  {
    \"functionName\": \"homeControl\",
    \"arguments\": [\"controlledDevice\", \"controlledState\"]
  },
  {
    \"functionName\": \"ledStripMusicSync\",
    \"arguments\": []
  },
  {
    \"functionName\": \"setLedStripLightColour\",
    \"arguments\": [\"rgbColourCode\", \"brightnessValue\"]
  },
  {
    \"functionName\": \"setLedStripLightSegmentColour\",
    \"arguments\": [\"segmentName\", \"rgbColourCode\", \"brightnessValue\"]
  },
  {
    \"functionName\": \"computerVisionActivation\",
    \"arguments\": [\"feature\", \"state\"]
  }
]

Guidelines:
Focus on actionable tasks or requests within the transcript.
Use the closest matching function name from the predefined list.
If no suitable function is found, set functionName to null and arguments to an empty object.
For matched actions, extract and assign argument values as intelligently as possible from the transcript.
Ignore small talk or non-actionable statements.

#### Output Format (Strict JSON, Do Not Exceed This Format):
[
  {
    "action": "<Action description>",
    "functionName": "<function_name or null>",
    "arguments": {
      // key-value pairs of arguments, or empty if none
    }
  }
  // ...additional actions
]

[/INST] Input:
"""

voice_transcript = "Please open Notepad and write an article about OpenAI in 250 words."

response = client.responses.create(
    model="gpt-4.1",
    input=f"{prompt_template} {voice_transcript}"
)

print(response.output_text)
