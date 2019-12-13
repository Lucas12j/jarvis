Para ambos os SOs, a versão 3.8 do python não é compatível com as dependências. Recomendo o uso da versão 3.6 da linguagem para garantir o perfeito funcionamento.  


Será necessário a instalação das seguintes bibliotecas/APi (excluindo as dependências que cada uma possa ter): 

-SpeechRecognition  |  pip install SpeechRecognition
-wikipedia          |  pip install  wikipedia
-pyttsx3            |  pip install pyttsx3
-pyaudio            |  sudo apt-get install python-pyaudio



Será necessário também a instalação de um sintetizador de voz, neste projeto por padrão estou usando o eSpeak, segue o link para dowload do mesmo:

http://espeak.sourceforge.net/download.html




-*-*-*-*-IMPORTANTÍSSIMO:-*-*-*-*-

 	Caso você esteja usando o Anaconda3 (assim como usei para trabalhar no projeto), provavelmente terá problemas ao executar o pyaudio.
 	Depois de muito pesquisar, descobri que provavelmente há uma inconpatibilidade na biblioteca "portaudio" enviada pelo anaconda. 
 	Resolvi o problema usando o seguinte comando: conda install nwani::portaudio nwani::pyaudio

 	Não sei se terão esse problema usando outros meios, porém no anaconda se mostrou necessário.

 	Aqui está o link em que consegui a resolução do problema, ali acharão maiores detalhes -> https://github.com/ContinuumIO/anaconda-issues/issues/4139




OBS:
    ----Windows----

    *Como o software foi pensado e programado para o linux, alguns erros de formatação podem ocorrer na leitura do arquivo .csv "dialogos".
    *Será necessário a instalação de algumas dependências relacionadas as bibliotecas usadas no projeto. 

    ----Linux(Ubunto)----

    *Posteriormente estarei disponibilizando um script que fará a instalação do software automaticamente.



Att: Lucas da Silva dos Santos

