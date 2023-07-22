package com.chat.chatserver.controller;

import com.chat.chatserver.model.Message;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

@Controller
public class ChatController {

    @Autowired
    private SimpMessagingTemplate simpMessagingTemplate;

    @MessageMapping("/message") // Mapeamento do endpoint WebSocket
    @SendTo("/chatroom/public") // Envia a resposta para o tópico "/chatroom/public"
    public Message receivePublicMessage(@Payload Message message) {
        return message;
    }

    @MessageMapping("/private-message")
    public Message receivePrivateMessage(@Payload Message message) {

        simpMessagingTemplate.convertAndSendToUser(message.getReceiverName(), "/private", message);
        return message;
    }
}

/*Ha um controlador WebSocket (@Controller) que recebe mensagens enviadas para o endpoint
 "/chatroom/public" através da anotação @MessageMapping. O parâmetro do método receivePublicMessage é anotado com @Payload,
 indicando que o valor do objeto message deve ser extraído da carga (payload) da mensagem.
Após processar a mensagem, o controlador responde enviando 'message' para o tópico "/chatroom/public", definido pela
 anotação @SendTo.*/
