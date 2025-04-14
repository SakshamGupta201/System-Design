class TextEditor:
    def bold(self):
        print("Text made Bold")

    def italic(self):
        print("Text made Italic")


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class BoldCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor = editor

    def execute(self):
        self.editor.bold()

    def undo(self):
        print("Bold reverted")


class ItalicCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.italic()

    def undo(self):
        print("Italic reverted")


class TextEditorInvoker:
    def __init__(self):
        self.commands = []
        self.undo_stack: list[Command] = []

    def execute_commands(self, command: Command):
        command.execute()
        self.commands.append(command)
        self.undo_stack.append(command)

    def undo_last_command(self):
        if self.undo_stack:
            last_cmd = self.undo_stack.pop()
            last_cmd.undo()


if __name__ == "__main__":
    editor = TextEditor()
    bold_command = BoldCommand(editor)
    italic_command = ItalicCommand(editor)
    
    invoker = TextEditorInvoker()
    
    invoker.execute_commands(bold_command)
    invoker.execute_commands(italic_command)
    
    invoker.undo_last_command()
    invoker.undo_last_command()