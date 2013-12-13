#ifndef STRATEGIAPROVE_H
#define STRATEGIAPROVE_H

#include "ui_strategiaprove.h"

#include "barbero.h"

class StrategiaProveDialog : public QDialog {

    Q_OBJECT

public:
    StrategiaProveDialog(QWidget* parent = 0);
    ~StrategiaProveDialog();

public slots:
    void FillCombo(QStringList fantini, QStringList contrade, Barbero* contrada, int* status);
    void enableCombo1(int state);
    void enableCombo2(int state);
    void enableCombo3(int state);

private:
    Ui::StrategiaProve ui;

};

#endif // STRATEGIAPROVE_H
