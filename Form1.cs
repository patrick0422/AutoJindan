using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoJindan
{
    public partial class Form1 : Form
    {
        public const string VERSION = "1.2";

        public Form1()
        {
            InitializeComponent();

            Text = "난 건강해 v." + VERSION;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
        }

        private void buttonStart_Click(object sender, EventArgs e)
        {
            if (!File.Exists("user.txt"))
            {
                MessageBox.Show("먼저 정보를 설정해 주세요.");

                return;
            }

            Process.Start("Jindan.exe");
        }

        private void button2_User(object sender, EventArgs e)
        {
            new User().ShowDialog();
        }
    }
}
