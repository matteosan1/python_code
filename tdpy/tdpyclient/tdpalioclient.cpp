#include "tdpalioclient.h"

#include <QtNetwork>
//#include <Phonon>

#include "nuovogiocatore.h"
#include "CaricaGiocoDialog.h"
#include "ServerConnectionDialog.h"
#include "TrattaDialog.h"
#include "SceltaFantino.h"
#include "Profilo.h"

//FIXME secondo me va spostato
#include "ListaVittorie.h"

#include <QGraphicsScene>
#include <QGraphicsPixmapItem>
#include <QSound>

#include <QMessageBox>
#include <QFileDialog>
#include <QInputDialog>
#include <QSound>

#include <QHeaderView>
#include <QKeySequence>

#include <QTimer>

#include <iostream>
using namespace std;

void TDPalioClient::ready() {
  std::cout << "READY???????" << std::endl;
  sendMessage(Ready);
}

void TDPalioClient::becomeSpectator() {
    sendMessage(Spettatore);
}

void TDPalioClient::startGame() {
  sendMessage(Start);
}

void TDPalioClient::chooseContrada() {
    sendMessage(AddPlayer);
}

void TDPalioClient::closeEvent(QCloseEvent* event) {
    //int ret = QMessageBox::question(this, tr("TDPalio Client"),
    //				  tr("Sei sicuro di voler uscire ?"),
    //			  QMessageBox::Ok);
    // if (ret == QMessageBox::Ok) {
    sendMessage(Disconnect);
    tcpSocket->disconnectFromHost();
    //} else {
    // return;
    //}
}

void TDPalioClient::sendMessage(MessageCode code) {

  std::cout << "CODICE SEND: " << code << std::endl;
  QByteArray block;
  QDataStream out(&block, QIODevice::WriteOnly);
  out.setVersion(QDataStream::Qt_4_0);
  
  // FIXME 
  //myStreamer->clear();
  myStreamer->socket_number = socket_number;
  myStreamer->code = code;
  std::cout << socket_number << std::endl;
  switch ((int)code) {
  case ScriviChat:
    break;
  case UserName:
    myStreamer->stringStream.push_back(giocatore.userName());
    break;
  case AggiornaContradaPanel:
    break;
  case Tratta:
    break;
  case Ready:
    break;
  case Vittorie:
    break;
  case AddPlayer:
    break;
  case NewPlayer:
    myStreamer->giocatoreStream = giocatore;
    break;
  case Start:
    break;
  case Spettatore:
    break;
  case FileName:
    break;
  case NomeAlFantino:
    break;
  case Disconnect:
    break;
  }

  std::cout << "1!" << std::endl;
  out << (*myStreamer);
  std::cout << "2!" << std::endl;
  tcpSocket->write(block);
  std::cout << "3!" << std::endl;
}

void TDPalioClient::incomingMessage() {

    QDataStream in(tcpSocket);
    in.setVersion(QDataStream::Qt_4_0);
    processMessage(in);
}

void TDPalioClient::processMessage(QDataStream& in) {
  
  while(1) {
    in >> (*myStreamer);
    std::cout << "CODICE RECV:" << (int)myStreamer->code << std::endl;
    switch((int)myStreamer->code) {  
    case LeggiChat:
      {
	leggiChat(myStreamer->stringStream);
	break;
      }
    case AggiornaListaChat:
      {
	listaChat = myStreamer->stringListStream[0];
	break;
      }
    case AggiornaCavalloPanel:
      {
	aggiornaCavalloPanel(myStreamer->cavalloStream[0]);
	break;
      }
    case AggiornaContradaPanel:
      {
	aggiornaContradaPanel(myStreamer->contradaStream[0]);
	break;
      }
    case ScegliFantino:
      {
	break;
      }
    case NomeAlFantino:
      {
	battesimo();
	break;
      }
    case Tratta:
      {
	sceltaCavalli(myStreamer->intStream[0], myStreamer->cavalloStream);
	break;
      }
      
    case Vittorie:
      {
	visualizzaTabellaVittorie(&myStreamer->contradaStream, 1);
	break;
      }
    case Initialize:
      {
	socket_number = myStreamer->socket_number;
	// condizionare il tasto di avvio
	if (myStreamer->intStream[0] == 0)
	  ui.actionAvvia_gioco->setEnabled(true);
	sendMessage(UserName);
	//if (myStreamer->intStream[0] == 1)
	//ui.actionScegli_Contrada->setEnabled(true);
	break;
      }
    case ChooseGame:
      {
	nuovoGioco(myStreamer->stringListStream[0],
		   myStreamer->stringListStream[1]);
	break;
      }
    case Estrazione:
      {
	visualizzaEstrazione(myStreamer->stringListStream[0]);
	break;
      }
    case Assegnazione:
      {
	visualizzaAssegnazione(myStreamer->intStream, 
			       myStreamer->stringStream,
			       myStreamer->cavalloStream);
	break;
      }
    case PopupMessage:
      {
	QMessageBox::information(this, tr("TDPalio Client"),
				 tr(myStreamer->stringStream[0].toLatin1()));
	break;
      }
    case Message:
      {
	QString mex1 = QDateTime::currentDateTime().time().toString();
	mex1 = mex1 + " - " + myStreamer->stringStream[0].toLatin1();
	textStatus->append(tr(mex1.toLatin1()));
	break;
      }
    case ChooseContrada:
      {
	ui.actionAvvia_gioco->setEnabled(false);
	ui.actionSpettatore->setEnabled(false);
	ui.actionScegli_Contrada->setEnabled(true);
	//QStringList lista;
	//QVector<int> index;
	//in >> lista;
	//in >> index;
	nuovoGiocatore(myStreamer->stringListStream[0],
		       myStreamer->intStream);
	ui.actionSpettatore->setEnabled(true);
	ui.actionScegli_Contrada->setEnabled(false);
	break;
      }
    }
    
    if (in.atEnd())
      break;
  }
}

void TDPalioClient::visualizzaTabellaCavalli() {
  // intestazione comune
  // numero cavallo - nome

  // visualizza la tabella solo se sei nel momento opportuno 
  // diciamo tra tratta e assegnazione

  // apri la finestra
  // anzi prima interroga il server per la lista completa dei cavalli
  // FIXME aggiungi stemma comune
}

void TDPalioClient::visualizzaTabellaVittorie(QVector<Contrada>* c, int a = -1) {
  if (a == -1)
    sendMessage(Vittorie);
  else {
    // FIXME se la finestra e` non modale devo farlo diventare un 
    // puntatore globale
    ListaVittorie lv(c, this);
    lv.exec();    
  }
}

void TDPalioClient::visualizzaTabellaCuffie() {
  // barberino contrada
  // nome - astinenza - data ultimo palio vinto
  // in ordine di cuffia

  // apri la finestra
  // anzi prima interroga il server per la lista completa dei cavalli
  // FIXME aggiungi stemma comune
}

void TDPalioClient::visualizzaStatusContrada() {
  // popolazione
  // soldi
  // eventuale fantino di contrada
  // rapporto con le altre contrade
  // gradimento capitano
  


  // apri la finestra
  // anzi prima interroga il server per la lista completa dei cavalli
  // FIXME aggiungi stemma comune
}

void TDPalioClient::visualizzaTabellaFantini() {
  // nome di battesimo ????
  // nome di battaglia
  // vittorie - capacita` - prezzo

  // apri la finestra
  // anzi prima interroga il server per la lista completa dei cavalli
  // FIXME aggiungi stemma comune
}

void TDPalioClient::visualizzaAssegnazione(QVector<int> indices, QVector<QString> contrade, QVector<Cavallo> cavalli) {

  // FIXME usare il timer per il suono e poi anche per 
  // l'estrazione con le bandiere...
  QTimer timer;

  
  QStringList list;
  //if (soundWanted)
  //  QSound::play("../tdpalioclient/sound/chiarine.wav");
  //sleep(10);
  
  int posx[10] = {130, 130, 130, 130, 130, 588, 588, 588, 588, 588};
  int posy[10] = {220, 259, 295, 339, 380, 220, 259, 295, 339, 380};
  int posConx[10] = {175, 175, 175, 175, 175, 630, 630, 630, 630, 630};
  int posCony[10] = {220, 259, 295, 339, 380, 220, 259, 295, 339, 380};

  statusBar()->showMessage("Assegnazione");
  //ui.label->show();
  
  QGraphicsPixmapItem* tabelle_contrade[10];
  QGraphicsPixmapItem* tabelle_coscia[10];
  
  QGraphicsScene* scene = new QGraphicsScene(ui.frame);

  scene->setSceneRect(0, 0, 906, 616);
  
  ui.graphicsView->setScene(scene);
  ui.graphicsView->setRenderHint(QPainter::Antialiasing);
  ui.graphicsView->setBackgroundBrush(QPixmap(":/assegnazione/pictures/tabellone.jpg"));
  //view.setCacheMode(QGraphicsView::CacheBackground);
  //view.setDragMode(QGraphicsView::ScrollHandDrag);

  // FIXME da verificare
  //ui.graphicsView->scale((float)ui.graphicsView->width()/906., (float)ui.graphicsView->height()/616.);
  
  // FIXME carica numeri e nomi e converti disegni in gif
  for(int i=0; i<10; ++i) {
    QString s = QString(":/assegnazione/pictures/tabellone_") + contrade[indices[i]].toLower() + QString(".png");
    tabelle_contrade[i] = scene->addPixmap(s);
    tabelle_contrade[i]->setPos(posConx[i], posCony[i]);
    
    s = QString(":/assegnazione/pictures/tabellone_%1").arg(cavalli[i].coscia()+1) + QString(".png");
    tabelle_coscia[i] = scene->addPixmap(s);
    tabelle_coscia[i]->setPos(posx[i], posy[i]);
    tabelle_coscia[i]->show();
  } 

  for(int i=0; i<10; i++) {
    for(int j=0; j<10; j++) {
      if (indices[j] == i)
	list << cavalli[j].getNome();
    }
  }
  
  ui.graphicsView->show();  
  
  //if(soundWanted)
  /*
  VoceSindaco voceSindaco;
  for(int i=0; i<10; i++) {
    QString s1 = QString("../tdpalioclient/sound/%1.wav").arg(indices[i+10]+1);
    QString s2 = QString("../tdpalioclient/sound/")+contrade[indices[i]].toLower()+QString(".wav");
    
    voceSindaco.caricaSuoni(s1, s2);
  }

  QTimer *timer = new QTimer();
  connect(timer, SIGNAL(timeout()), &voceSindaco, SLOT(playSound()));

  for(int i=0; i<10; i++) 
    timer->start(1000);
  */
  //tabelle_contrade[i]->show();
  //ui.graphicsView->show();
  //ui.graphicsView->update();
  
  aggiornaContradeTabel(2, list);
}
  
void TDPalioClient::visualizzaEstrazione(QStringList list) {
  
  int posx[17] = {140, 190, 240, 290, 340, 390, 440, 490, 550, 625, 190, 240, 290, 340, 390, 440, 490};
  int posy[17] = {440, 440, 440, 440, 440, 440, 440, 440, 440, 440, 220, 220, 220, 220, 220, 220, 215};
  
  statusBar()->showMessage("Estrazione delle Contrade");
  //ui.label->show();
  
  QGraphicsPixmapItem* bandiere[17];
  QGraphicsScene* scene = new QGraphicsScene(ui.frame);
  for(int i=0; i<17; ++i) {
    QString s = ":/estrazione/pictures/" + list[i] + "_1.gif";
    bandiere[i] = scene->addPixmap(s);
    bandiere[i]->setPos(posx[i], posy[i]);
  }
  
  scene->setSceneRect(0, 0, 906, 616);
  
  ui.graphicsView->setScene(scene);
  ui.graphicsView->setRenderHint(QPainter::Antialiasing);
  ui.graphicsView->setBackgroundBrush(QPixmap(":/estrazione/pictures/palazzo_comunale.jpg"));
  //view.setCacheMode(QGraphicsView::CacheBackground);
  //view.setDragMode(QGraphicsView::ScrollHandDrag);
  // FIXME dimensioni rispetto alla finestra principale
  ui.graphicsView->scale((float)ui.graphicsView->width()/906., (float)ui.graphicsView->height()/616.);
  ui.graphicsView->show();
  
  for(int i=0; i<7; ++i) 
    bandiere[i]->show();
  
  //if (soundWanted)
  //  QSound::play("../tdpalioclient/sound/chiarine.wav");
  // FIXME
  //sleep(10);
  
  for(int i=7; i<10; ++i) {
    bandiere[i]->show();
    //sleep(3);
  }

  aggiornaContradeTabel(1, list);
}

void TDPalioClient::aggiornaContradeTabel(int type, QStringList list) {

  switch(type) {
  case 1:
    {
      for(int i=0; i<10; i++) {
	QString s = "../tdpalioclient/pictures/barbero_"+list[i].toLower()+"_small.png";
	QTableWidgetItem* item = new QTableWidgetItem(QIcon(s), "");
	ui.tableWidget_contrade->setItem(i, 0, item);
      }
      break;
    }  
  case 2:
    {
      for(int i=0; i<10; i++) {
	QTableWidgetItem* item = new QTableWidgetItem(list[i]);
	//item->setForeground(Qt::blue);
	ui.tableWidget_contrade->setItem(i, 1, item);
      }
      break;
    }
  }
}

void TDPalioClient::nuovoGioco(QStringList nomi, QStringList date) {

  // FIXME gestire estensione del file
  CaricaGiocoDialog cg(nomi, date, this);

  number_int = cg.exec();

  if (number_int == 2)
    text_string = nomi[cg.getSelection()];
  else
    text_string = QInputDialog::getText(this, tr("Nuovo Gioco"), tr("Nome"));

  myStreamer->clear();
  myStreamer->intStream.push_back(number_int);
  myStreamer->stringStream.push_back(text_string);

  sendMessage(FileName);
}

void TDPalioClient::nuovoGiocatore(QStringList lista, QVector<int> index) {

  if (index[0] != -1) { 
    NuovoGiocatoreDialog ng(this);
    ng.setContrade(lista, index);
    
    if (ng.exec() == QDialog::Accepted) {
      // FIXME troppo complicato perche` scomodare giocatore ????
      giocatore.setContrada(ng.getGiocatore().contrada());
      sendMessage(NewPlayer);
      sendMessage(AggiornaContradaPanel);
    }
  } else {
    // FIXME migliorare la scritta
    giocatore.setContrada(index[1]);
    QString mex = "In questa partita sei capitano della Contrada: " + lista[0];
    QMessageBox::information(this, tr("TDPalio Client"), mex);
    giocatore.setGioca();
    sendMessage(NewPlayer);
    sendMessage(AggiornaContradaPanel);
    sendMessage(Ready);
  }
}

void TDPalioClient::aggiornaCavalloPanel(Cavallo c) {

  std::cout << c.forma() << std::endl;
  ui.label_cavallo->setText("Cavallo: "+c.getNome());
  QString s = QString("Corsi: %1").arg(c.paliCorsi());
  ui.label_cavalloCorsi->setText(s);
  s = QString("Vinti: %1").arg(c.paliVinti());
  ui.label_cavalloVinti->setText(s);  
  ui.progressBar_forma->setValue(c.forma()*10);
}

void TDPalioClient::aggiornaContradaPanel(Contrada c) {

  QString s = "../tdpalioclient/pictures/barbero_"+c.getNome().toLower()+"_big.png";
  ui.label_pngContrada->setPixmap(s);
  ui.label_nomeContrada->setText(c.getNomeCompleto());
  s = QString("Mandato: %1").arg(giocatore.tempo());
  ui.label_carica->setText(s);
  s = QString("Umore: %1\%").arg(c.umore());
  ui.label_gradimento->setText(s);
}


void TDPalioClient::displayError(QAbstractSocket::SocketError socketError) {
  switch (socketError) {
  case QAbstractSocket::RemoteHostClosedError:
    break;
  case QAbstractSocket::HostNotFoundError:
    QMessageBox::information(this, tr("TDPalio Client"),
			     tr("Impossibile connettersi al server. Controlla l'host e la porta."));
    break;
  case QAbstractSocket::ConnectionRefusedError:
    QMessageBox::information(this, tr("TDPalio Client"),
			     tr("La connessione e` stata rifiutata dal server. Controlla che il server sia attivo. Controlla l'host e la porta."));
    break;
  default:
    QMessageBox::information(this, tr("TDPalio Client"),
			     tr("Errore: %1.")
			     .arg(tcpSocket->errorString()));
  }
}

/*


QString TDPalio::getData() {
    QString s = "Palio del ";

    switch(mese) {
        case Luglio:
            s += "2 Luglio ";
            break;
        case Agosto:
            s += "16 Agosto ";
            break;
        case Straordinario:
            // scegliere giorno e mese casuali
            s += "17 Settembre ";
            break;
    }
    s += QString::number(anno);
    return s;
}

void TDPalio::filePrint() {

}

void TDPalio::close() {

    salvaCorrente();
    QMainWindow::close();
}
*/

void TDPalioClient::aiutoInformazioni() {
  QMessageBox::about(this, tr("Informazioni TDPalio"),
		     tr("<h2>TDPalio 2.0</h2>"
			"<p>Copyright &copy 2007 MatteoSoftware<br>"
			"<p>TDPalio e` il gioco manageriale del Palio di Siena"));
  
}

void TDPalioClient::abilitaSuono(bool a) {
  soundWanted = a;
}

void TDPalioClient::sceltaCavalli(int q, QVector<Cavallo> cavalli) {
  
  std::cout << "SCELTI:" << q << std::endl;
  TrattaDialog t(q, &cavalli, this);
  t.exec();

  myStreamer->clear();
  myStreamer->intStream = t.getSelection();
  sendMessage(Tratta);
}

void TDPalioClient::sceltaFantino(int q, QVector<Fantino> fantini) {
  
  SceltaFantino t(q, &fantini, this);
  t.exec();
  
  myStreamer->clear();
  //myStreamer->intStream = t.getSelection();
  sendMessage(ScegliFantino);
}

void TDPalioClient::battesimo() {
  
  QString titolo = myStreamer->stringStream[0];
  QString text;
  bool ok = false;
  while(!ok) {
    text = QInputDialog::getText(this, tr("Segnatura del Fantino"),
				 titolo + QString("\nNome di Battaglia:"),
				 QLineEdit::Normal,
				 QDir::home().dirName(), 
				 &ok);

    if (!ok || text.isEmpty()) {
      QMessageBox::critical(this, tr("TDPalio Error"),
			    tr("Non puoi non specificare un nome !"),
			    QMessageBox::Ok);
    }
  }
  myStreamer->stringStream[0] = text;
  sendMessage(NomeAlFantino);

  return ;
}

void TDPalioClient::chiudiChat() {
  ui.lineEdit_chat->setEnabled(false);
  ui.chatEdit->setVisible(false);
  ui.lineEdit_chat->setVisible(false);
  ui.lineEdit_chat->setText("");
  chatPeer = "";
}

void TDPalioClient::apriChat() {
  
  bool ok;
  QString item = QInputDialog::getItem(this, tr("Chat"), tr("Contrada"),
				       listaChat, 0, false, &ok);
  
  QStringList list1 = item.split(" -");
  chatPeer = list1[0];
  if (ok && !item.isEmpty()) {
    ui.lineEdit_chat->setEnabled(true);
    ui.chatEdit->setVisible(true);
    ui.lineEdit_chat->setVisible(true);
    ui.lineEdit_chat->setFocus();
  }  
}

void TDPalioClient::scriviChat() {
  
  QString real_text  = giocatore.userName() + ": " + ui.lineEdit_chat->text() + "<br>";
  myStreamer->stringStream.resize(3);
  myStreamer->stringStream[0] = chatPeer;
  myStreamer->stringStream[1] = giocatore.userName();
  myStreamer->stringStream[2] = real_text;
  
  ui.chatEdit->setTextColor(Qt::blue);
  ui.chatEdit->insertHtml(real_text);
  ui.lineEdit_chat->setText("");
  // FIXME 
  //QString total_text = ui.lineEdit_chat->toHtml();
  //total_text = total_text("<a name=\"end\"", "");
  //ui.chatEdit->insertHtml(real_text);
  
  sendMessage(ScriviChat);
}

void TDPalioClient::leggiChat(QVector<QString> s) {
  ui.lineEdit_chat->setEnabled(true);
  ui.chatEdit->setVisible(true);
  ui.lineEdit_chat->setVisible(true);
  ui.lineEdit_chat->setFocus();
  ui.chatEdit->setTextColor(Qt::red);
  ui.chatEdit->insertHtml(s[2]);
  chatPeer = s[1];
}
