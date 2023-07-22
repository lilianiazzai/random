package com.chat.chatserver.model;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Message {
    private String senderName;
    private String receiverName;
    private String message;
    private String date;
    private Status status;
}

/*não é necessário escrever manualmente os métodos
 getters, setters, construtores ou toString()
 devido ao Lombok*/