from transformers import AutoProcessor, BarkModel
import scipy
import gradio as gr

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

def submit(prompt, voice, filename):
    if len(prompt) == 0:
        return {error_box: gr.Textbox(value="Enter prompt", visible=True)}
    #voice_preset = "v2/en_speaker_6"
    inputs = processor(prompt, voice_preset=voice)#_preset)

    audio_array = model.generate(**inputs)
    audio_array = audio_array.cpu().numpy().squeeze()

    sample_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write(f"/output/{filename}", rate=sample_rate, data=audio_array)

    return {
        output_row: gr.Row(visible=True),
        text_out: "DONE",
        audio_out: f'/output/{filename}'
    }

with gr.Blocks() as demo:
    error_box = gr.Textbox(label="Error", visible=False)

    with gr.Row():
        drop_voices = gr.Dropdown(["v2/en_speaker_1", "v2/en_speaker_2", "v2/en_speaker_3", "v2/en_speaker_4", "v2/en_speaker_5", "v2/en_speaker_6", "v2/en_speaker_7", "v2/en_speaker_8", "v2/en_speaker_9"], label="voices 1-8 male/9 female", value=0)
        file_in = gr.Textbox(label="file", value="test.wav")
    with gr.Row():
        text_in = gr.Textbox(label="prompt")
    with gr.Row():
        submit_btn = gr.Button("Submit")
    with gr.Row(visible=True) as output_row:
        text_out = gr.Textbox(label="output")
        audio_out = gr.Audio(label="generated")
    submit_btn.click(
        submit,
        [text_in, drop_voices, file_in],
        [error_box, text_out, audio_out, output_row],
    )

demo.queue() 
demo.launch(share=True, show_api=False)
    
