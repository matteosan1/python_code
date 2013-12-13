#include "ServerConnectionDialog.h"

ServerConnectionDialog::ServerConnectionDialog(QWidget* parent) : QDialog(parent) {

    ui.setupUi(this);
    
    host = "localhost";
    port = 1974;
    connect(ui.lineEdit, SIGNAL(textChanged(QString)), this, SLOT(text1(QString)));
    connect(ui.lineEdit_2, SIGNAL(textChanged(QString)), this, SLOT(text2(QString)));
    connect(ui.checkBox, SIGNAL(stateChanged(int)), this, SLOT(localConnection(int)));
}

void ServerConnectionDialog::text1(QString t) {
  host = t;
}

void ServerConnectionDialog::text2(QString t) {
  port = t.toInt();
}

void ServerConnectionDialog::localConnection(int a) {
  if (a == 0) {
    ui.lineEdit->setEnabled(true);
    ui.lineEdit_2->setEnabled(true);
    local = 0;
  }
  
  if (a == 2) {
    ui.lineEdit->setEnabled(false);
    ui.lineEdit_2->setEnabled(false);
    host = "localhost";
    port = 1974;
    local = 1;
  }
}
