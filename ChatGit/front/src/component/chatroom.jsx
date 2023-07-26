import { useState } from 'react'
import stomps from 'stompjs'
import SockJS from 'sockjs-client'
import { saveDataToLocalStorage, loadDataFromLocalStorage } from './LocalStorageUtils';

var stompClient = null;

const ChatRoom = () => {    
    
    const [publicChats, setpublicChats] = useState([]);
    const [privateChats, setPrivateChats] = useState(new Map());
    const [tab, setTab] = useState("CHATROOM");
    const [userData, setUserData] = useState({
        username: "",
        receivername: "",
        connected:false,
        message: ""
    })

    const handleValue = (event)=>{
        const {value, name} = event.target;
        setUserData({...userData, [name]:value});
    }

    /* Essa função atribui um par ordenado assim q um evento ocorre (nesse caso, o botão é apertado);
    e adiciona-o juntamente aos anteriores, de forma a atualizar os dados do usuario*/

    const registerUser = ()=>{
        let Sock = new SockJS('http://localhost:8181/ws')
        // termina com ws pq no backend, arquivo WebSocketConfig definimos ao stomp o
        // endpoint como sendo ws

        /* Cria uma instancia do SockJS, que basicamente providencia um cliente WebS p navegador */

        stompClient = stomps.over(Sock);
        /* Cria um cliente stomp recebendo o cliente WebS como argumento */
        stompClient.connect({}, onConnected, onError);

        /*Função para verificar se a conexão foi estabelecida com sucesso */
    }


    /* Função chamda apos a conexao ter sido estabelecida com sucesso!
    Inscreve o usuario em dois endereços WebS */
    const onConnected = ()=>{
        setUserData({...userData, "connected":true})
        /*atualizando o status dos usuarios para conectado */

        stompClient.subscribe('/chatroom/public', onPublicMessageReceived);
        stompClient.subscribe('/user/'+userData.username+'/private', onPrivateMessageReceived);
        /* Permite que o usuario receba msgs desses endereços */

        userJoin();
    }

    // Avisa o servidor quando um usuario entra
    const userJoin = ()=>{
        
        let chatMessage = {
            senderName: userData.username,
            status: 'JOIN'
        };
        
        stompClient.send('/app/message', {}, JSON.stringify(chatMessage));
        /* Convertendo a mensagem para JSON string (WebS trata msg como string) e mandando para esse endereço */
        
    }
    
    // Função p lidar com erros
    const onError = (err)=>{
        console.log(err);
    }

    // payload é a msg recebida do WebS dps do metodo no back
    const onPublicMessageReceived = (payload)=>{
        let payloadData = JSON.parse(payload.body);
        // convertendo p objeto

        switch(payloadData.status) {
            case "JOIN":
                // Caso seja a primeira pessoa a entrar no chat
                if (!privateChats.get(payloadData.senderName)) {
                    privateChats.set(payloadData.senderName, []);
                    // adiciona-se ao mapa sendo o username a chave

                    setPrivateChats(new Map (privateChats));
                    // atualiza o mapa após a inserção do usuario
                }
                break;

            case "MESSAGE":
                publicChats.push(payloadData);
                // adicionando a msg ao array publicChats

                setpublicChats([...publicChats]);
                break;
        }
    }

    // payload é a mensagem recebida do servidor WebS
    // Essa função é chamada quando uma msg é recebida em /user/username/private
    const onPrivateMessageReceived = (payload) => {
        console.log(payload);
        let payloadData = JSON.parse(payload.body); //converte p objeto
    
        // Condicional que verifica se já existe um chat privado para o usuário
        if (privateChats.get(payloadData.senderName)) {
            // se o chat existir, a msg recebida é adicionada na array
            privateChats.get(payloadData.senderName).push(payloadData);
            setPrivateChats(new Map(privateChats));
            // atualiza o chat privado com a nova mensagem
        } else {
            // caso não exista, criamos um chat (representado por array)
            // e adicionamos a msg recebida
            let list = [];
            list.push(payloadData);
        
            privateChats.set(payloadData.senderName, list);
            setPrivateChats(new Map(privateChats));
            // adicionamos a entrada (username) no privateChats e instanciamos um mapa
        }
    };
  

    const sendPublicMessage = ()=>{
        // Verifica se a conexão foi estabelecida com sucesso
        if (stompClient) {
            // Representa a msg p servidor WebS
            let chatMessage = {
                senderName: userData.username,
                message: userData.message,
                status: 'MESSAGE'
            };
            stompClient.send('/app/message', {}, JSON.stringify(chatMessage));
            // Converte a msg para JSON string e envia p esse endereço
            setUserData({...userData, "message": ""});
            // Depois do envio, limpamos o input 
        }
    }

    const sendPrivateMessage = ()=>{
        if (stompClient) {
            let chatMessage = {
                senderName: userData.username,
                receiverName: tab,
                message: userData.message,
                status: 'MESSAGE'
            };

            // Verifica se o usuario nao esta mandando msg p si msm
            if (userData.username !== tab) {
                // privateChats é um mapa cujas chave sao os usernames de quem recebe
                privateChats.get(tab).push(chatMessage);
                // adiciona-se a msg ao array
                setPrivateChats(new Map(privateChats));
            }
            stompClient.send('/app/private-message', {}, JSON.stringify(chatMessage));
            // Apos isso, enviamos a msg ao WebS p esse endpoint no servidor
            setUserData({...userData, "message": ""});
        }
    }


    return (
        <div className='container'>
            {userData.connected?
            <div className='chat-box'>

                <div className='member-list'>
                    <ul>
                        <li onClick={() => { setTab("CHATROOM") }} className={`member ${tab === "CHATROOM" && "active"}`}>Bate-Papo</li>
                        {[...privateChats.keys()].map((name, index) => (
                        <li onClick={() => { setTab(name) }} className={`member ${tab === name && "active"}`} key={index}>
                            {name}
                        </li>
                        ))}
                    </ul>
                </div>

                {tab === "CHATROOM" && <div className = 'chat-content'>
                    <ul className='chat-messages'>
                    {publicChats.map((chat, index)=>(
                        <li className = 'message' key = {index}>
                            {chat.senderName !== userData.username && <div className='avatar'>{chat.senderName}</div>}
                                <div className='message-data'>{chat.message}</div>
                            {chat.senderName === userData.username && <div className='avatar self'>{chat.senderName}</div>}
                        </li>
                    ))}
                    </ul>

                    <div className='send-message'>
                        <input type='text' className='input-message'
                            name='message' placeholder='digite uma mensagem pública' value={userData.message}
                            onChange={handleValue} />
                        <button type='button' className='send-button' onClick={sendPublicMessage}>enviar</button>

                    </div>

                    </div>}
                {tab !== "CHATROOM" && <div className = 'chat-content'>
                <ul className='chat-messages'>
                    {[...privateChats.get(tab)].map((chat, index)=>(
                        <li className = 'message' key = {index}>
                            {chat.senderName !== userData.username && <div className='avatar'>{chat.senderName}</div>}
                            <div className='message-data'>{chat.message}</div>
                            {chat.senderName === userData.username && <div className='avatar self'>{chat.senderName}</div>}
                        </li>
                    ))}
                    </ul>

                    <div className='send-message'>
                        <input type='text' className='input-message'
                            name = 'message' placeholder={`digite uma mensagem para ${tab}`} value={userData.message}
                            onChange={handleValue} />
                        <button type='button' className='send-button' onClick={sendPrivateMessage}>enviar</button>

                    </div>

                </div>}

            </div>
            :
            <div className='register'>
                <input
                id='user-name'
                name = 'username'
                placeholder='nome de usuário'
                value={userData.username}
                onChange={handleValue}
                />

                <button type='button' onClick={registerUser}>
                    conectar
                </button>

            </div>}
        </div>  
    )
}

export default ChatRoom