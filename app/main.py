from nicegui import ui
from qrcodegen import generate_qr_code
import re

@ui.page('/')
def index():
    ui.page_title('QR Code Generator')
    
    global current_filename

    dark = ui.dark_mode()
    dark.value = True
    with ui.row().classes('w-full justify-end'):    
        ui.switch('Dark Mode').bind_value(dark)

    with ui.column().classes('items-center w-full mt-10 gap-3'):
        ui.label('QR Code Generator').classes('text-2xl')

    
        url_input = ui.input(label='Enter URL', 
            placeholder='example.com'
            ).props('clearable rounded outlined size=70').style('font-size: 1.0rem;')
        

        qr_image = ui.image().classes('w-64 h-64')
        qr_image.style("display: none")

        def generate():
            global current_filename
            url = (url_input.value or "")
            
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
            qr_image.style("display: block")
            
            # hide button before generating QR code
            download_button.style("display: block") 
        
        def download():
            if current_filename:
                ui.download.file(current_filename)
            else:
                ui.notify("Generate a QR code first", type='warning')
            pass
        
        ui.button('Generate QR Code', on_click=generate).classes('mt-2')
        
        download_button = ui.button('Download QR Code', on_click=download)
        download_button.style("display: none")
    
ui.run()
