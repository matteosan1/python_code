#include "strategiaprove.h"

#include <iostream>
using namespace std;

StrategiaProveDialog::StrategiaProveDialog(QWidget* parent)
    : QDialog(parent) {

    // signals and slots connections
    //connect( okButton, SIGNAL( clicked() ), this, SLOT( accept() ) );
    //connect( cancelButton, SIGNAL( clicked() ), this, SLOT( reject() ) );
    //connect( scelta1Check, SIGNAL( stateChanged(int) ), this, SLOT( enableCombo1(int) ) );
    //connect( scelta2Check, SIGNAL( stateChanged(int) ), this, SLOT( enableCombo2(int) ) );
    //connect( scelta3Check, SIGNAL( stateChanged(int) ), this, SLOT( enableCombo3(int) ) );
}

StrategiaProveDialog::~StrategiaProveDialog()
{}


void StrategiaProveDialog::FillCombo(QStringList fantini,
                                     QStringList contrade,
                                     Barbero* contrada, int* status) {

    ui.contrada1Combo->addItems(contrade);
    ui.contrada2Combo->addItems(contrade);
    ui.contrada3Combo->addItems(contrade);

    for(int i=0; i<fantini.size(); ++i) {
        if (status[i] == 1) {
            ui.scelta1Combo->addItem(QPixmap(":/icons/pictures/filenew.png"), fantini[i]);
            ui.scelta2Combo->addItem(QPixmap(":/icons/pictures/filenew.png"), fantini[i]);
            ui.scelta3Combo->addItem(QPixmap(":/icons/pictures/filenew.png"), fantini[i]);
        } else {
            ui.scelta1Combo->addItem(fantini[i]);
            ui.scelta2Combo->addItem(fantini[i]);
            ui.scelta3Combo->addItem(fantini[i]);
        }
    }

    ui.contradaLabel->setText(contrada->getContrada()->getNomeCompleto());
    QString monta;
    if (contrada->getFantino() != 0)
        monta = contrada->getFantino()->getNome();
    else
        monta = "nessun fantino scelto.";

    ui.montaLabel->setText("Monta attuale: "+monta);
    ui.cavalloLabel->setText(contrada->getCavallo()->getNome());
    ui.formaBar->setTextVisible(true);
    // FIXME ci vorra` anche il range ?????
    //ui.formaBar->setRange(0, 100);
    ui.formaBar->setValue(contrada->forma());

    QStringList strategia;
    strategia << "Mossa" << "Spunto" << "Curve";

    //for(unsigned int i=0; i<contrade.size(); i++)
    //strategia.append("Ostacola " + contrade[i]);
    ui.primaCombo->addItems(strategia);
    ui.secondaCombo->addItems(strategia);
    ui.terzaCombo->addItems(strategia);
    ui.quartaCombo->addItems(strategia);
    ui.generaleCombo->addItems(strategia);
    ui.acciaCombo->addItems(strategia);
}

void StrategiaProveDialog::enableCombo1( int state ) {
    ui.contrada1Combo->setEnabled(state);
}

void StrategiaProveDialog::enableCombo2( int state ) {
    ui.contrada2Combo->setEnabled(state);
}

void StrategiaProveDialog::enableCombo3( int state ) {
    ui.contrada3Combo->setEnabled(state);
}

