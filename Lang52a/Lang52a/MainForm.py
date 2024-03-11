import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DodgerBlue
		self._textBox1.Location = System.Drawing.Point(58, 54)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(109, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DodgerBlue
		self._textBox2.Location = System.Drawing.Point(303, 54)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(108, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label1.Location = System.Drawing.Point(58, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Length"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label2.Location = System.Drawing.Point(303, 28)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(108, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Width"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SteelBlue
		self._button1.Location = System.Drawing.Point(72, 243)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(95, 39)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SteelBlue
		self._button2.Location = System.Drawing.Point(189, 243)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(95, 39)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SteelBlue
		self._button3.Location = System.Drawing.Point(303, 243)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(95, 39)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label3.Location = System.Drawing.Point(58, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(109, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Area"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label4.Location = System.Drawing.Point(303, 115)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(108, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Perimeter"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.DodgerBlue
		self._label5.Location = System.Drawing.Point(58, 147)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(109, 23)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DodgerBlue
		self._label6.Location = System.Drawing.Point(303, 147)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(108, 23)
		self._label6.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MidnightBlue
		self.ClientSize = System.Drawing.Size(473, 304)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width 
		perim = 2 * length + 2 * width
		self._label5.Text = str(area)
		self._label6.Text = str(perim)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()