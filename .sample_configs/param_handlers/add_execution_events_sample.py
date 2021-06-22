def make_execution(execution: str) -> str:
    execution = execution

    return execution

def make_events(artifact: str) -> typing.Sequence[google.cloud.aiplatform_v1beta1.types.event.Event]:
    events = [{'artifact': artifact}]

    return events

