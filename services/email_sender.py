import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Carrega EMAIL_USER, EMAIL_PASS e EMAIL_TO do .env
load_dotenv()

def enviar_email(nome_completo: str, corpo: str) -> bool:
    """
    Envia um e-mail com o assunto 'DS-160 - {nome_completo}' e corpo texto.
    Retorna True se enviado com sucesso, False caso contrário.
    """
    remetente    = os.getenv("EMAIL_USER")
    senha        = os.getenv("EMAIL_PASS")
    destinatario = os.getenv("EMAIL_TO", remetente)  # se não houver EMAIL_TO, usa o próprio remetente

    if not remetente or not senha:
        print("Variáveis EMAIL_USER e EMAIL_PASS devem estar definidas no .env")
        return False

    # Monta a mensagem
    msg = MIMEMultipart()
    msg["From"]    = remetente
    msg["To"]      = destinatario
    msg["Subject"] = f"DS-160 - {nome_completo}"
    msg.attach(MIMEText(corpo, "plain"))

    # Envia via Gmail SSL
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False
