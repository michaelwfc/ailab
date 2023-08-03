import gradio as gr


def greet(name):
    return "Hello " + name + "!"


def run_greet_interface():
    demo = gr.Interface(fn=greet, inputs="text", outputs="text")
    demo.launch()


# greet_block_demo:
# with gr.Blocks() as demo:
#     gr.Markdown(
#         """
#     # Hello World!
#     Start typing below to see the output.
#     """)
#     # The Blocks app code will be contained within this clause.
#     name_input = gr.Textbox(
#         label="Name", placeholder="Input name ...", lines=3)
#     output = gr.Textbox(label="Output Box")

#     # the click() event listener. Event listeners define the data flow within the app.
#     # In the example above, the listener ties the two Textboxes together.
#     # greet_btn = gr.Button("Greet")
#     # greet_btn.click(fn=greet, inputs=name_input,
#     #                 outputs=output, api_name="greet")

#     # the welcome function is triggered by typing in the Textbox inp. This is due to the change() event listener.
#     name_input.change(greet, name_input, output)


with gr.Blocks(theme=gr.themes.Default()) as demo:
    food_box = gr.Number(value=10, label="Food Count")
    status_box = gr.Textbox()

    def eat(food):
        if food > 0:
            return {food_box: food - 1, status_box: "full"}
        else:
            return {status_box: "hungry"}

    eat_button = gr.Button("EAT")
    eat_button.click(
        fn=eat,
        inputs=food_box,
        outputs=[food_box, status_box]
    )


if __name__ == "__main__":
    # demo = get_demo()
    demo.launch()
