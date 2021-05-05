/********************************************************************************
** Form generated from reading UI file 'calc.ui'
**
** Created by: Qt User Interface Compiler version 6.0.4
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CALC_H
#define UI_CALC_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_calc
{
public:
    QWidget *centralwidget;
    QGridLayout *gridLayout;
    QPushButton *Multiply;
    QPushButton *Button9;
    QPushButton *MemClear;
    QPushButton *Button1;
    QPushButton *Button7;
    QPushButton *Button6;
    QPushButton *Button5;
    QPushButton *Button2;
    QPushButton *MemGet;
    QPushButton *Button4;
    QPushButton *Add;
    QPushButton *MemAdd;
    QLineEdit *Display;
    QPushButton *Divide;
    QPushButton *Button3;
    QPushButton *Button8;
    QPushButton *Clear;
    QPushButton *Button0;
    QPushButton *ChangeSign;
    QPushButton *Subtract;
    QPushButton *Equals;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *calc)
    {
        if (calc->objectName().isEmpty())
            calc->setObjectName(QString::fromUtf8("calc"));
        calc->resize(269, 299);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(calc->sizePolicy().hasHeightForWidth());
        calc->setSizePolicy(sizePolicy);
        centralwidget = new QWidget(calc);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayout = new QGridLayout(centralwidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        Multiply = new QPushButton(centralwidget);
        Multiply->setObjectName(QString::fromUtf8("Multiply"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(Multiply->sizePolicy().hasHeightForWidth());
        Multiply->setSizePolicy(sizePolicy1);
        Multiply->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Multiply, 3, 3, 1, 1);

        Button9 = new QPushButton(centralwidget);
        Button9->setObjectName(QString::fromUtf8("Button9"));
        sizePolicy1.setHeightForWidth(Button9->sizePolicy().hasHeightForWidth());
        Button9->setSizePolicy(sizePolicy1);
        Button9->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button9, 2, 2, 1, 1);

        MemClear = new QPushButton(centralwidget);
        MemClear->setObjectName(QString::fromUtf8("MemClear"));
        sizePolicy1.setHeightForWidth(MemClear->sizePolicy().hasHeightForWidth());
        MemClear->setSizePolicy(sizePolicy1);
        MemClear->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(MemClear, 3, 4, 1, 1);

        Button1 = new QPushButton(centralwidget);
        Button1->setObjectName(QString::fromUtf8("Button1"));
        sizePolicy1.setHeightForWidth(Button1->sizePolicy().hasHeightForWidth());
        Button1->setSizePolicy(sizePolicy1);
        Button1->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button1, 4, 0, 1, 1);

        Button7 = new QPushButton(centralwidget);
        Button7->setObjectName(QString::fromUtf8("Button7"));
        sizePolicy1.setHeightForWidth(Button7->sizePolicy().hasHeightForWidth());
        Button7->setSizePolicy(sizePolicy1);
        Button7->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button7, 2, 0, 1, 1);

        Button6 = new QPushButton(centralwidget);
        Button6->setObjectName(QString::fromUtf8("Button6"));
        sizePolicy1.setHeightForWidth(Button6->sizePolicy().hasHeightForWidth());
        Button6->setSizePolicy(sizePolicy1);
        Button6->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button6, 3, 2, 1, 1);

        Button5 = new QPushButton(centralwidget);
        Button5->setObjectName(QString::fromUtf8("Button5"));
        sizePolicy1.setHeightForWidth(Button5->sizePolicy().hasHeightForWidth());
        Button5->setSizePolicy(sizePolicy1);
        Button5->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button5, 3, 1, 1, 1);

        Button2 = new QPushButton(centralwidget);
        Button2->setObjectName(QString::fromUtf8("Button2"));
        sizePolicy1.setHeightForWidth(Button2->sizePolicy().hasHeightForWidth());
        Button2->setSizePolicy(sizePolicy1);
        Button2->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button2, 4, 1, 1, 1);

        MemGet = new QPushButton(centralwidget);
        MemGet->setObjectName(QString::fromUtf8("MemGet"));
        sizePolicy1.setHeightForWidth(MemGet->sizePolicy().hasHeightForWidth());
        MemGet->setSizePolicy(sizePolicy1);
        MemGet->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(MemGet, 4, 4, 1, 1);

        Button4 = new QPushButton(centralwidget);
        Button4->setObjectName(QString::fromUtf8("Button4"));
        sizePolicy1.setHeightForWidth(Button4->sizePolicy().hasHeightForWidth());
        Button4->setSizePolicy(sizePolicy1);
        Button4->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button4, 3, 0, 1, 1);

        Add = new QPushButton(centralwidget);
        Add->setObjectName(QString::fromUtf8("Add"));
        sizePolicy1.setHeightForWidth(Add->sizePolicy().hasHeightForWidth());
        Add->setSizePolicy(sizePolicy1);
        Add->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Add, 4, 3, 1, 1);

        MemAdd = new QPushButton(centralwidget);
        MemAdd->setObjectName(QString::fromUtf8("MemAdd"));
        sizePolicy1.setHeightForWidth(MemAdd->sizePolicy().hasHeightForWidth());
        MemAdd->setSizePolicy(sizePolicy1);
        MemAdd->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(MemAdd, 2, 4, 1, 1);

        Display = new QLineEdit(centralwidget);
        Display->setObjectName(QString::fromUtf8("Display"));
        sizePolicy.setHeightForWidth(Display->sizePolicy().hasHeightForWidth());
        Display->setSizePolicy(sizePolicy);
        QFont font;
        font.setFamily(QString::fromUtf8("Comic Sans MS"));
        font.setPointSize(12);
        font.setBold(true);
        Display->setFont(font);
        Display->setStyleSheet(QString::fromUtf8("QLineEdit {\n"
"background-color: black;\n"
"border: 1px blue;\n"
"color:#FFFFFF ;\n"
"}"));
        Display->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        gridLayout->addWidget(Display, 0, 0, 1, 5);

        Divide = new QPushButton(centralwidget);
        Divide->setObjectName(QString::fromUtf8("Divide"));
        sizePolicy1.setHeightForWidth(Divide->sizePolicy().hasHeightForWidth());
        Divide->setSizePolicy(sizePolicy1);
        Divide->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Divide, 2, 3, 1, 1);

        Button3 = new QPushButton(centralwidget);
        Button3->setObjectName(QString::fromUtf8("Button3"));
        sizePolicy1.setHeightForWidth(Button3->sizePolicy().hasHeightForWidth());
        Button3->setSizePolicy(sizePolicy1);
        Button3->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button3, 4, 2, 1, 1);

        Button8 = new QPushButton(centralwidget);
        Button8->setObjectName(QString::fromUtf8("Button8"));
        sizePolicy1.setHeightForWidth(Button8->sizePolicy().hasHeightForWidth());
        Button8->setSizePolicy(sizePolicy1);
        Button8->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button8, 2, 1, 1, 1);

        Clear = new QPushButton(centralwidget);
        Clear->setObjectName(QString::fromUtf8("Clear"));
        sizePolicy1.setHeightForWidth(Clear->sizePolicy().hasHeightForWidth());
        Clear->setSizePolicy(sizePolicy1);
        Clear->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Clear, 5, 0, 1, 1);

        Button0 = new QPushButton(centralwidget);
        Button0->setObjectName(QString::fromUtf8("Button0"));
        sizePolicy1.setHeightForWidth(Button0->sizePolicy().hasHeightForWidth());
        Button0->setSizePolicy(sizePolicy1);
        Button0->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Button0, 5, 1, 1, 1);

        ChangeSign = new QPushButton(centralwidget);
        ChangeSign->setObjectName(QString::fromUtf8("ChangeSign"));
        sizePolicy1.setHeightForWidth(ChangeSign->sizePolicy().hasHeightForWidth());
        ChangeSign->setSizePolicy(sizePolicy1);
        ChangeSign->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#00FF00;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#32CD32;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(ChangeSign, 5, 2, 1, 1);

        Subtract = new QPushButton(centralwidget);
        Subtract->setObjectName(QString::fromUtf8("Subtract"));
        sizePolicy1.setHeightForWidth(Subtract->sizePolicy().hasHeightForWidth());
        Subtract->setSizePolicy(sizePolicy1);
        Subtract->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Subtract, 5, 3, 1, 1);

        Equals = new QPushButton(centralwidget);
        Equals->setObjectName(QString::fromUtf8("Equals"));
        sizePolicy1.setHeightForWidth(Equals->sizePolicy().hasHeightForWidth());
        Equals->setSizePolicy(sizePolicy1);
        Equals->setStyleSheet(QString::fromUtf8("QPushButton {\n"
"background-color:#FF00FF;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color:#9932CC;\n"
"border: 1px blue;\n"
"padding: 5px;\n"
"}"));

        gridLayout->addWidget(Equals, 5, 4, 1, 1);

        calc->setCentralWidget(centralwidget);
        menubar = new QMenuBar(calc);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 269, 21));
        calc->setMenuBar(menubar);
        statusbar = new QStatusBar(calc);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        calc->setStatusBar(statusbar);

        retranslateUi(calc);

        QMetaObject::connectSlotsByName(calc);
    } // setupUi

    void retranslateUi(QMainWindow *calc)
    {
        calc->setWindowTitle(QCoreApplication::translate("calc", "calc", nullptr));
        Multiply->setText(QCoreApplication::translate("calc", "*", nullptr));
        Button9->setText(QCoreApplication::translate("calc", "9", nullptr));
        MemClear->setText(QCoreApplication::translate("calc", "M-", nullptr));
        Button1->setText(QCoreApplication::translate("calc", "1", nullptr));
        Button7->setText(QCoreApplication::translate("calc", "7", nullptr));
        Button6->setText(QCoreApplication::translate("calc", "6", nullptr));
        Button5->setText(QCoreApplication::translate("calc", "5", nullptr));
        Button2->setText(QCoreApplication::translate("calc", "2", nullptr));
        MemGet->setText(QCoreApplication::translate("calc", "M", nullptr));
        Button4->setText(QCoreApplication::translate("calc", "4", nullptr));
        Add->setText(QCoreApplication::translate("calc", "+", nullptr));
        MemAdd->setText(QCoreApplication::translate("calc", "M+", nullptr));
        Display->setText(QCoreApplication::translate("calc", "0,0", nullptr));
        Divide->setText(QCoreApplication::translate("calc", "/", nullptr));
        Button3->setText(QCoreApplication::translate("calc", "3", nullptr));
        Button8->setText(QCoreApplication::translate("calc", "8", nullptr));
        Clear->setText(QCoreApplication::translate("calc", "AC", nullptr));
        Button0->setText(QCoreApplication::translate("calc", "0", nullptr));
        ChangeSign->setText(QCoreApplication::translate("calc", "+/-", nullptr));
        Subtract->setText(QCoreApplication::translate("calc", "-", nullptr));
        Equals->setText(QCoreApplication::translate("calc", "=", nullptr));
    } // retranslateUi

};

namespace Ui {
    class calc: public Ui_calc {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CALC_H
