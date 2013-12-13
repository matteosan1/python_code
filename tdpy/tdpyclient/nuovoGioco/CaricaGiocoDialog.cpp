#include "CaricaGiocoDialog.h"

#include <QMessageBox>

CaricaGiocoDialog::CaricaGiocoDialog(QStringList nomi, QStringList date, QWidget* parent) : QDialog(parent), n(nomi), d(date) {

    ui.setupUi(this);

    ui.tableFile->setRowCount(n.size());
    ui.tableFile->setColumnCount(2);

    ui.tableFile->setEditTriggers(QAbstractItemView::NoEditTriggers);
    ui.tableFile->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui.tableFile->setSelectionMode(QAbstractItemView::SingleSelection);

    QStringList headerLabels;
    headerLabels << "Nome" << "Data Creazione";
    ui.tableFile->setHorizontalHeaderLabels(headerLabels);

    populateTable();

    ui.tableFile->resizeColumnsToContents();
    //ui.cavalliView->resize(500, 300);
    // ui.tableFile->show();

    connect(ui.tableFile, SIGNAL(itemSelectionChanged()), this,SLOT(enableButton()));
    connect(ui.caricaButton, SIGNAL(clicked()), this, SLOT(load()));
    connect(ui.cancellaButton, SIGNAL(clicked()), this, SLOT(esci()));
 
}

void CaricaGiocoDialog::load() {
  QDialog::done(2);
}

void CaricaGiocoDialog::esci() {
  QDialog::done(3);
}

void CaricaGiocoDialog::populateTable() {

    for(int i=0; i<n.size(); ++i) {
        QTableWidgetItem* item0 = new QTableWidgetItem(n[i]);
        QTableWidgetItem* item1 = new QTableWidgetItem(d[i]);
        ui.tableFile->setItem(i, 0, item0);
        ui.tableFile->setItem(i, 1, item1);
    }
}

CaricaGiocoDialog::~CaricaGiocoDialog()
{}

void CaricaGiocoDialog::enableButton() {
    ui.caricaButton->setEnabled(true);
}

int CaricaGiocoDialog::getSelection() {

  int result = ui.tableFile->currentRow();
  return result;
}
