/* =====================================================
   FUNÇÃO PARA ENVIAR UMA MENSAGEM PARA O WHATSAPP
   ===================================================== */

function enviarWhatsApp() {

    /* -------------------------------------------------
       Número do WhatsApp que receberá a mensagem.
       Deve estar no formato internacional:
       País + DDD + Número
       Exemplo do Brasil:
       55 16 99999-9999
    ------------------------------------------------- */
    var numeroWhatsApp = "55016991659459";


    /* -------------------------------------------------
       Captura as informações digitadas pelo usuário
       no formulário HTML.
       O método getElementById procura um elemento
       pelo seu id e o ".value" pega o texto digitado.
    ------------------------------------------------- */

    var nome = document.getElementById("nome").value;

    var email = document.getElementById("email").value;

    var assunto = document.getElementById("assunto").value;

    var mensagem = document.getElementById("mensagem").value;


    /* -------------------------------------------------
       Junta todas as informações em uma única mensagem.
       "\n" significa quebra de linha.
    ------------------------------------------------- */

    var mensagemFormatada =
        "Nome: " + nome +
        "\nEmail: " + email +
        "\nAssunto: " + assunto +
        "\n\nMensagem: " + mensagem;


    /* -------------------------------------------------
       Remove os espaços em branco da mensagem.
       replace() procura todos os espaços (" ")
       e substitui por nada ("").

       Obs.: Esta linha normalmente NÃO é necessária,
       pois ela deixa o texto sem espaços.
       Se desejar manter a mensagem legível,
       basta remover esta linha.
    ------------------------------------------------- */

    mensagemFormatada = mensagemFormatada.replace(/ /g, "");


    /* -------------------------------------------------
       Cria o endereço (URL) que será enviado ao
       WhatsApp.

       encodeURIComponent() converte caracteres
       especiais para que o navegador consiga
       interpretar corretamente a mensagem.
    ------------------------------------------------- */

    var linkWhatsApp =
        "https://wa.me/" +
        numeroWhatsApp +
        "?text=" +
        encodeURIComponent(mensagemFormatada);


    /* -------------------------------------------------
       Abre uma nova aba do navegador contendo
       a conversa do WhatsApp já preenchida.
    ------------------------------------------------- */

    window.open(linkWhatsApp, "_blank");


    /* -------------------------------------------------
       Exibe uma caixa de aviso informando
       que a mensagem foi enviada para o WhatsApp.
    ------------------------------------------------- */

    alert("Mensagem enviada para o WhatsApp!");
}
