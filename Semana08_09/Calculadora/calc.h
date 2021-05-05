//Igor Augusto - 11221EMT008
#ifndef calc_H
#define calc_H

#include <QMainWindow>

namespace Ui {
class calc;
}

class calc : public QMainWindow
{

    Q_OBJECT

public:


    explicit calc(QWidget *parent = 0);
    ~calc();

private:
    Ui::calc *ui;


private slots :
    void NumPressed();
    void MathButtonPressed();
    void EqualButtonPressed();
    void ChangeNumberSign();
};
#endif // calc_H
