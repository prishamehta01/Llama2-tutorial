
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/prishamehta/Llamma2Tutorial/workflows/workflow-577496"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="71e12aa1b2e845dbb5afdfd6ec8bac72"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
