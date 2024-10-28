import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def send_email(address):
    #Dane do uwierzytelnienia
    smtp_server = ''
    smtp_port = 587
    smtp_user = ''
    smtp_password = ''


    msg = MIMEMultipart()
    msg['From'] = 'DotDesign <noreply@dotd.pl>'
    msg['To'] = address
    msg['Subject'] = 'Zabujaj się w nowych fotelach DotDesign'

    #Treść wiadomości
    msg.attach(MIMEText('''

    <body style="font-family: Arial, Helvetica, sans-serif; background-color: #f9f9f9; margin: 0; padding: 0;">
    <div style="max-width: 600px; margin: 0 auto; padding: 20px; background-color: #ffffff; border-radius: 10px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #0a5c0a; text-align: center;">ZABUJAJ SIĘ OD PIERWSZEGO SIEDZENIA W NAJNOWSZEJ KOLEKCJI FOTELI BUJANYCH OD DOTDESIGN</h1>
        <p style="font-size: 16px; line-height: 1.5; color: #333333;">Słyszysz „fotel bujany" i myślisz o przestarzałych wiklinowych bujakach na płozach? Mimo że mogą wywoływać nostalgię, ich era już minęła. Poznaj innowacyjną alternatywę w postaci stylowych, komfortowych i funkcjonalnych foteli bujanych od DotDesign.</p>
        <div style="text-align: center; width: 100%;">
            <a href="https://dotd.pl/wp-content/uploads/2024/06/16.png" target="_blank">
                <img src="https://dotd.pl/wp-content/uploads/2024/06/16.png" alt="bujane" style="width: 300px; height: 300px; display: block; margin: auto;">
            </a>
        </div>
        <p style="font-size: 16px; line-height: 1.5; color: #333333;">Koniec z trzeszczeniem, uwieraniem i rysami na podłodze, pora pobujać w obłokach... Przedstawiamy produkty, jakich jeszcze nie było na polskim rynku meblarskim! Z kodem „BUJAJSIE" zyskujesz 10 procent rabatu na fotele bujane z naszej najnowszej kolekcji. Zapraszamy na zakupy!</p>

        <div style="text-align: center; margin-top: 20px;">
            <h1 style="border: 2px dashed black; padding: 10px; display: inline-block; margin-bottom: 20px;">BUJAJSIE</h1>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://dotd.pl" style="display: inline-block; padding: 10px 20px; background-color: #0a5c0a; color: #ffffff; text-decoration: none; border-radius: 5px;">Sprawdź ofertę</a>
        </div>
        <p style="font-size: 16px; line-height: 1.5; color: #333333;">Pozdrawiamy, DotDesign</p>
        <p style="font-size: 16px; line-height: 1.5; color: #333333;">*Kod rabatowy nie łączy się z innymi promocjami</p>
    </div>
</body>
    ''', 'html'))

    #Nagłówki
    msg.add_header('X-Mailer', 'My Mailer')
    msg.add_header('X-Priority', '1')
    msg['Priority'] = '1'

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, address, msg.as_string())
        print(f'Wysłano mail do: {address}')
    except Exception as e:
        print(f'Błąd podczas wysyłania maila do {address}: {str(e)}')


if __name__ == "__main__":
    with open('adresy.txt', 'r') as plik_adresy:
        adresy_email = plik_adresy.read().splitlines()

    for adres_email in adresy_email:
        send_email(adres_email)
        time.sleep(18)
