#ifndef SERVERCONNECTION_H
#define SERVERCONNECTION_H

#include "ui_serverconnection.h"

#include <QString>

class ServerConnectionDialog : public QDialog {
    Q_OBJECT

 public:
  ServerConnectionDialog(QWidget* parent = 0);
  ~ServerConnectionDialog() {}

  int getPort() { return port; }
  QString getHost() { return host; }
  int getLocal() { return local; }

  public slots:
  void text1(QString);
  void text2(QString);
  void localConnection(int);
	
 private:

    Ui::serverConnection ui;
    QString host;
    int port;
    int local;
};

#endif
