from nicegui import ui
from qrcodegen import generate_qr_code

current_filename = None


@ui.page('/')
def index():
    ui.page_title('QR Code Generator')
    global current_filename

    with ui.column().classes('items-center justify-center h-screen w-full'):
        ui.label('QR Code Generator').classes('text-2xl')

        url_input = ui.input(
            label='Enter URL',
            placeholder='https://example.com'
        )

        qr_image = ui.image().classes('w-64 h-64')

        def generate():
            global current_filename
            url = (url_input.value or '').strip()

            if not url:
                ui.notify("URL cannot be empty", type='warning')
                return
            
            current_filename = generate_qr_code(url)
            qr_image.set_source(current_filename)

        def download():
            if current_filename:
                ui.download.file(current_filename)
            else:
                ui.notify("Generate a QR code first", type='warning')

        ui.button('Generate QR Code', on_click=generate)
        ui.button('Download QR Code', on_click=download)
ui.run()
