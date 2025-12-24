from nicegui import ui
from qrcodegen import generate_qr_code
import re

@ui.page('/')
def index():
    ui.page_title('QR Code Generator')
    
    
    global current_filename

    with ui.column().classes('items-center justify-center h-screen w-full'):
        ui.label('QR Code Generator').classes('text-2xl')

    
        url_input = ui.input(label='Enter URL', 
            placeholder='https://example.com'
            ).props('clearable rounded outlined dense size=70')
        

        qr_image = ui.image().classes('w-64 h-64')

        def generate():
            global current_filename
            url = (url_input.value or "").strip() # remove trailing whitespace
            
            #url validation
            if not url:
                ui.notify("URL can't be empty", type='warning')
                return
            
            if not re.match(
                r'^(https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}([\/\w .-]*)*\/?$', url):
                ui.notify("Invalid URL: Please enter a valid URL")
                return
           
            current_filename = generate_qr_code(url)
            qr_image.set_source(current_filename)
            
            # hide button before generating QR code
            download_button.style("display: block") 
        
        def download():
            if current_filename:
                ui.download.file(current_filename)
            else:
                ui.notify("Generate a QR code first", type='warning')
            pass
        
        ui.button('Generate QR Code', on_click=generate)
        
        download_button = ui.button('Download QR Code', on_click=download)
        download_button.style("display: none")
    
ui.run()
