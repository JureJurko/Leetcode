from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_request(self, doc) -> None:
        pass

class Document:
    def __init__(self):
        self.state = Draft()
        self.approved = False

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State) -> None:
        self.state = state

    def publish(self) -> None:
        self.state.handle_request(self)

    def set_approval(self, approved: bool) -> None:
        self.approved = approved

    def is_approved(self) -> bool:
        return self.approved

class Draft(State):
    def handle_request(self, doc: Document) -> None:
        doc.state = Review()

class Review(State):
    def handle_request(self, doc: Document) -> None:
        approval = doc.approved

        if approval:
            doc.state = Published()
        else:
            doc.state = Draft()

class Published(State):
    def handle_request(self, doc: Document) -> None:
        return
