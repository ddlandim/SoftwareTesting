#include <QtTest>
#include <QCoreApplication>

// add necessary includes here

class Triangle : public QObject
{
    Q_OBJECT

public:
    Triangle();
    ~Triangle();

private slots:
    void initTestCase();
    void cleanupTestCase();
    void test_case1();
};

Triangle::Triangle()
{

}

Triangle::~Triangle()
{

}

void Triangle::initTestCase()
{

}

void Triangle::cleanupTestCase()
{

}

void Triangle::test_case1()
{

}

QTEST_MAIN(Triangle)

#include "tst_triangle.moc"
