/********************************************************************************
** Form generated from reading ui file 'killplayer.ui'
**
** Created: Tue Sep 25 01:41:19 2007
**      by: Qt User Interface Compiler version 4.3.0
**
** WARNING! All changes made in this file will be lost when recompiling ui file!
********************************************************************************/

#ifndef UI_KILLPLAYER_H
#define UI_KILLPLAYER_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QComboBox>
#include <QtGui/QDialog>
#include <QtGui/QDialogButtonBox>
#include <QtGui/QLabel>

class Ui_KillPlayer
{
public:
    QDialogButtonBox *buttonBox;
    QLabel *label;
    QComboBox *comboBox;

    void setupUi(QDialog *KillPlayer)
    {
    if (KillPlayer->objectName().isEmpty())
        KillPlayer->setObjectName(QString::fromUtf8("KillPlayer"));
    QSize size(400, 300);
    size = size.expandedTo(KillPlayer->minimumSizeHint());
    KillPlayer->resize(size);
    buttonBox = new QDialogButtonBox(KillPlayer);
    buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
    buttonBox->setGeometry(QRect(30, 240, 341, 32));
    buttonBox->setOrientation(Qt::Horizontal);
    buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::NoButton|QDialogButtonBox::Ok);
    label = new QLabel(KillPlayer);
    label->setObjectName(QString::fromUtf8("label"));
    label->setGeometry(QRect(110, 40, 191, 18));
    comboBox = new QComboBox(KillPlayer);
    comboBox->setObjectName(QString::fromUtf8("comboBox"));
    comboBox->setGeometry(QRect(130, 80, 161, 22));

    retranslateUi(KillPlayer);
    QObject::connect(buttonBox, SIGNAL(accepted()), KillPlayer, SLOT(accept()));
    QObject::connect(buttonBox, SIGNAL(rejected()), KillPlayer, SLOT(reject()));

    QMetaObject::connectSlotsByName(KillPlayer);
    } // setupUi

    void retranslateUi(QDialog *KillPlayer)
    {
    KillPlayer->setWindowTitle(QApplication::translate("KillPlayer", "Elimina Giocatore", 0, QApplication::UnicodeUTF8));
    label->setText(QApplication::translate("KillPlayer", "TextLabel", 0, QApplication::UnicodeUTF8));
    Q_UNUSED(KillPlayer);
    } // retranslateUi

};

namespace Ui {
    class KillPlayer: public Ui_KillPlayer {};
} // namespace Ui

#endif // UI_KILLPLAYER_H
