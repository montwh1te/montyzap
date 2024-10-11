# Tela Inicial:
    # Título: Hashzap
    # Botão: Iniciar Chat
        # quando clicar no botão: 
        # abrir um popup/modal/alerta
            # Titulo: Bem vindo ao Hashzap
            # Caixa de Texto: Escreva seu nome no chat
            # Botão: Entrar no chat
                # quando clicar no botão
                # sumir com o titulo
                # sumir com o botão Iniciar Chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem:
                    # botão Enviar
                        # quando clicar no botão enviar
                        # enviar a mensagem
                        # limpar a caixa de mensagem
                        
# Flet
# importar o flet
import flet as ft

# criar uma função principal para rodar o seu aplicativo
def main(pagina):
    
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto.value)
        pagina.add(chat)
        pagina.update()
        
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
        
    def enviar_mensagem(evento):
        conteudo_texto = ft.Text(f"{text_box_popup.value}: {text_box_mensagem.value}")
        pagina.pubsub.send_all(conteudo_texto)
        # limpar caixa de mensagem
        text_box_mensagem.value = ""
        pagina.update()
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    def abrir_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(linha_enviar)
        aviso_entrada = ft.Text(f"{text_box_popup.value} entrou no Chat!")
        pagina.pubsub.send_all(aviso_entrada)
        pagina.update()
            
 
    # titulo
    titulo = ft.Text('Hashzap')
    pagina.add(titulo)
        
    # botao inicial
    botao = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup)
    pagina.add(botao)

    # criação do popup
    titulo_popup = ft.Text('Bem vindo ao Hashzap!')
    text_box_popup = ft.TextField(label='Escreva seu nome no chat...', on_submit=abrir_chat)
    botao_popup = ft.FilledButton('Entrar no chat', on_click=abrir_chat)
    popup = ft.AlertDialog(
            title=titulo_popup,
            content=text_box_popup,
            actions=[botao_popup]
        )
    
    # criação do chat
    text_box_mensagem = ft.TextField(label='Envie sua mensagem...', on_submit=enviar_mensagem)
    botao_chat = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    
    linha_enviar = ft.Row([text_box_mensagem, botao_chat])
    chat = ft.Column()
    
# executar essa função com o flet
ft.app(target=main, view=ft.AppView.WEB_BROWSER)