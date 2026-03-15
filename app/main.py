from nicegui import ui
from qrcodegen import generate_qr_code
import re
import os

@ui.page('/')
def index():
    ui.page_title('QR Code Generator')

    current_filename = None

    dark = ui.dark_mode()
    dark.value = True

    with ui.row().classes('w-full justify-end'):
        ui.switch('Dark Mode').bind_value(dark)

    with ui.column().classes('items-center w-full mt-10 gap-3'):

        ui.label('QR Code Generator').classes('text-2xl')

        url_input = ui.input(
            label='Enter URL',
            placeholder='example.com'
        ).props('clearable').style('font-size: 1.0rem;')
        

        qr_image = ui.image().classes('w-64 h-64')
        qr_image.style("display: none")

        def generate():
            nonlocal current_filename
            url = (url_input.value or "")

            if not url:
                ui.notify("URL can't be empty", type='warning')
                return

            if not re.match(
                r'^(https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}([\/\w .-]*)*\/?$', url):
                ui.notify("Invalid URL: Please enter a valid URL", type='warning')
                return

            current_filename = generate_qr_code(url)

            qr_image.set_source(current_filename)
            qr_image.style("display: block")

            download_button.style("display: block")
            delete_button.style("display: block")

            generate_button.style("display: none")

        def download():
            if current_filename:
                ui.download.file(current_filename)
            else:
                ui.notify("Generate a QR code first", type='warning')

        def delete_qr():
            nonlocal current_filename

            if current_filename and os.path.exists(current_filename):
                os.remove(current_filename)

            qr_image.style("display: none")

            download_button.style("display: none")
            delete_button.style("display: none")

            generate_button.style("display: block")

            current_filename = None

        with ui.row().classes('gap-4 mt-2'):

            generate_button = ui.button(
                'Generate QR Code',
                on_click=generate
            ).props('outline')

            download_button = ui.button(
                'Download QR Code',
                on_click=download
            ).props('outline')
            
            download_button.style("display: none")

            delete_button = ui.button(
                'Generate New QR Code',
                on_click=delete_qr
            ).props('outline')
            delete_button.style("display: none")

ui.run()