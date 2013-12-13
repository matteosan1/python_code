#ifndef CARICAGIOCODIALOG_H
#define CARICAGIOCODIALOG_H

#include "ui_caricagioco.h"

#include <QStringList>

class CaricaGiocoDialog : public QDialog {
    Q_OBJECT

public:
  CaricaGiocoDialog(QStringList nomi, QStringList date, QWidget* parent = 0);
    ~CaricaGiocoDialog();

    int getSelection();
    void populateTable();
	
public slots:
    void enableButton();
    void load();
    void esci();

private:

    Ui::CaricaGioco ui;
    QStringList n, d;
};

#endif
