import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.num1 = 0
		self.num2 = 0
		self.num3 = 0
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("Lottery.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._progressBar1 = System.Windows.Forms.ProgressBar()
		self._pictureBox8 = System.Windows.Forms.PictureBox()
		self._pictureBox9 = System.Windows.Forms.PictureBox()
		self._pictureBox10 = System.Windows.Forms.PictureBox()
		self._pictureBox1 = System.Windows.Forms.PictureBox()
		self._pictureBox2 = System.Windows.Forms.PictureBox()
		self._pictureBox3 = System.Windows.Forms.PictureBox()
		self._pictureBox4 = System.Windows.Forms.PictureBox()
		self._pictureBox5 = System.Windows.Forms.PictureBox()
		self._pictureBox6 = System.Windows.Forms.PictureBox()
		self._pictureBox7 = System.Windows.Forms.PictureBox()
		self._pictureBox11 = System.Windows.Forms.PictureBox()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._label3 = System.Windows.Forms.Label()
		self._pictureBox8.BeginInit()
		self._pictureBox9.BeginInit()
		self._pictureBox10.BeginInit()
		self._pictureBox1.BeginInit()
		self._pictureBox2.BeginInit()
		self._pictureBox3.BeginInit()
		self._pictureBox4.BeginInit()
		self._pictureBox5.BeginInit()
		self._pictureBox6.BeginInit()
		self._pictureBox7.BeginInit()
		self._pictureBox11.BeginInit()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackgroundImage = resources.GetObject("button1.BackgroundImage")
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._button1.Location = System.Drawing.Point(510, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(226, 247)
		self._button1.TabIndex = 2
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(510, 265)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(226, 41)
		self._button2.TabIndex = 3
		self._button2.Text = "Pickpocket"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(510, 313)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(64, 38)
		self._label1.TabIndex = 4
		self._label1.Text = "Bet"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(580, 326)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(155, 20)
		self._textBox1.TabIndex = 5
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(510, 366)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(64, 38)
		self._label2.TabIndex = 6
		self._label2.Text = "Cash"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# progressBar1
		# 
		self._progressBar1.Location = System.Drawing.Point(510, 415)
		self._progressBar1.Maximum = 1500
		self._progressBar1.Name = "progressBar1"
		self._progressBar1.Size = System.Drawing.Size(225, 23)
		self._progressBar1.TabIndex = 8
		# 
		# pictureBox8
		# 
		self._pictureBox8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox8.Location = System.Drawing.Point(13, 13)
		self._pictureBox8.Name = "pictureBox8"
		self._pictureBox8.Size = System.Drawing.Size(148, 205)
		self._pictureBox8.TabIndex = 9
		self._pictureBox8.TabStop = False
		# 
		# pictureBox9
		# 
		self._pictureBox9.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox9.Location = System.Drawing.Point(176, 12)
		self._pictureBox9.Name = "pictureBox9"
		self._pictureBox9.Size = System.Drawing.Size(148, 205)
		self._pictureBox9.TabIndex = 10
		self._pictureBox9.TabStop = False
		# 
		# pictureBox10
		# 
		self._pictureBox10.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox10.Location = System.Drawing.Point(340, 13)
		self._pictureBox10.Name = "pictureBox10"
		self._pictureBox10.Size = System.Drawing.Size(148, 205)
		self._pictureBox10.TabIndex = 11
		self._pictureBox10.TabStop = False
		# 
		# pictureBox1
		# 
		self._pictureBox1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._pictureBox1.BackgroundImage = resources.GetObject("pictureBox1.BackgroundImage")
		self._pictureBox1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox1.Location = System.Drawing.Point(13, 233)
		self._pictureBox1.Name = "pictureBox1"
		self._pictureBox1.Size = System.Drawing.Size(475, 205)
		self._pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
		self._pictureBox1.TabIndex = 12
		self._pictureBox1.TabStop = False
		self._pictureBox1.Visible = False
		# 
		# pictureBox2
		# 
		self._pictureBox2.BackgroundImage = resources.GetObject("pictureBox2.BackgroundImage")
		self._pictureBox2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox2.Location = System.Drawing.Point(25, 246)
		self._pictureBox2.Name = "pictureBox2"
		self._pictureBox2.Size = System.Drawing.Size(46, 42)
		self._pictureBox2.TabIndex = 13
		self._pictureBox2.TabStop = False
		self._pictureBox2.Visible = False
		# 
		# pictureBox3
		# 
		self._pictureBox3.BackgroundImage = resources.GetObject("pictureBox3.BackgroundImage")
		self._pictureBox3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox3.Location = System.Drawing.Point(77, 246)
		self._pictureBox3.Name = "pictureBox3"
		self._pictureBox3.Size = System.Drawing.Size(46, 42)
		self._pictureBox3.TabIndex = 14
		self._pictureBox3.TabStop = False
		self._pictureBox3.Visible = False
		# 
		# pictureBox4
		# 
		self._pictureBox4.BackgroundImage = resources.GetObject("pictureBox4.BackgroundImage")
		self._pictureBox4.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox4.Location = System.Drawing.Point(129, 246)
		self._pictureBox4.Name = "pictureBox4"
		self._pictureBox4.Size = System.Drawing.Size(46, 42)
		self._pictureBox4.TabIndex = 15
		self._pictureBox4.TabStop = False
		self._pictureBox4.Visible = False
		# 
		# pictureBox5
		# 
		self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
		self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox5.Location = System.Drawing.Point(181, 246)
		self._pictureBox5.Name = "pictureBox5"
		self._pictureBox5.Size = System.Drawing.Size(46, 42)
		self._pictureBox5.TabIndex = 16
		self._pictureBox5.TabStop = False
		self._pictureBox5.Visible = False
		# 
		# pictureBox6
		# 
		self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
		self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox6.Location = System.Drawing.Point(233, 246)
		self._pictureBox6.Name = "pictureBox6"
		self._pictureBox6.Size = System.Drawing.Size(46, 42)
		self._pictureBox6.TabIndex = 17
		self._pictureBox6.TabStop = False
		self._pictureBox6.Visible = False
		# 
		# pictureBox7
		# 
		self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
		self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox7.Location = System.Drawing.Point(25, 379)
		self._pictureBox7.Name = "pictureBox7"
		self._pictureBox7.Size = System.Drawing.Size(46, 42)
		self._pictureBox7.TabIndex = 18
		self._pictureBox7.TabStop = False
		self._pictureBox7.Visible = False
		# 
		# pictureBox11
		# 
		self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
		self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._pictureBox11.Location = System.Drawing.Point(77, 379)
		self._pictureBox11.Name = "pictureBox11"
		self._pictureBox11.Size = System.Drawing.Size(46, 42)
		self._pictureBox11.TabIndex = 19
		self._pictureBox11.TabStop = False
		self._pictureBox11.Visible = False
		# 
		# timer1
		# 
		self._timer1.Tick += self.Timer1Tick
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(580, 379)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(155, 23)
		self._label3.TabIndex = 20
		self._label3.Text = "100"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(747, 450)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._pictureBox11)
		self.Controls.Add(self._pictureBox7)
		self.Controls.Add(self._pictureBox6)
		self.Controls.Add(self._pictureBox5)
		self.Controls.Add(self._pictureBox4)
		self.Controls.Add(self._pictureBox3)
		self.Controls.Add(self._pictureBox2)
		self.Controls.Add(self._pictureBox1)
		self.Controls.Add(self._pictureBox10)
		self.Controls.Add(self._pictureBox9)
		self.Controls.Add(self._pictureBox8)
		self.Controls.Add(self._progressBar1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lottery"
		self._pictureBox8.EndInit()
		self._pictureBox9.EndInit()
		self._pictureBox10.EndInit()
		self._pictureBox1.EndInit()
		self._pictureBox2.EndInit()
		self._pictureBox3.EndInit()
		self._pictureBox4.EndInit()
		self._pictureBox5.EndInit()
		self._pictureBox6.EndInit()
		self._pictureBox7.EndInit()
		self._pictureBox11.EndInit()
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		rnd = System.Random()
		money = rnd.Next(1, 51)
		if money > 25:
			MessageBox.Show("You failed to steal money!")
		else:
			cmoney = float(self._label3.Text)
			self._label3.Text = str(round(cmoney + money, 2))
		pass

	def Button1Click(self, sender, e):
		im1 = self._pictureBox2.BackgroundImage
		im2 = self._pictureBox3.BackgroundImage
		im3 = self._pictureBox4.BackgroundImage
		im4 = self._pictureBox5.BackgroundImage
		im5 = self._pictureBox6.BackgroundImage
		levOff = self._pictureBox7.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		
		if self._textBox1.Text == "":
			MessageBox.Show("You must enter an amount to bet first!")
			return
		
		money = float(self._label3.Text)
		bet = float(self._textBox1.Text)
		money2 = money - bet
		
		if money == 0:
			MessageBox.Show("You have no money!")
		elif bet < 1:
			MessageBox.Show("You must bet at least 1 dollar!")
		elif bet > money and bet > money2:
			MessageBox.Show("You don't have enough money!")
		else:
			self._button1.BackgroundImage = levOn
			self._pictureBox1.Visible = True
			self._timer1.Enabled = True
			self._label3.Text = str(round(money2, 2))
			self._progressBar1.Value = 0
			
			num1 = self.num1
			num2 = self.num2 
			num3 = self.num3 
			
			if num1 == 1 and num2 == 1 and num3 ==1:
				money2 += bet * 2
			if num1 == 2 and num2 == 2 and num3 ==2:
				money2 += bet * 2
			if num1 == 3 and num2 == 3 and num3 ==3:
				money2 += bet * 2
			if num1 == 4 and num2 == 4 and num3 ==4:
				money2 += bet * 2
			if num1 == 5 and num2 == 5 and num3 ==5:
				money2 += bet * 100
			
			self.num1 = 0
			self.num2 = 0
			self.num3 = 0
			self._label2.Text = str(round(money2, 2))
			
			if money2 <= 0: 
				MessageBox.Show("You ran out of cash!")
		
		pass

	def Timer1Tick(self, sender, e):
		im1 = self._pictureBox2.BackgroundImage
		im2 = self._pictureBox3.BackgroundImage
		im3 = self._pictureBox4.BackgroundImage
		im4 = self._pictureBox5.BackgroundImage
		im5 = self._pictureBox6.BackgroundImage
		levOff = self._pictureBox7.BackgroundImage
		levOn = self._pictureBox11.BackgroundImage
		rnd = System.Random()
		num1 = 0
		num2 = 0
		num3 = 0
		
		pb1 = self._pictureBox8
		pb2 = self._pictureBox9
		pb3 = self._pictureBox10 
		
		for lcv in range(0, 1000):
			num1 = rnd.Next(1, 6)
			num2 = rnd.Next(1, 6)
			num3 = rnd.Next(1, 6)
			
			self.num1 = num1
			self.num2 = num2
			self.num3 = num3
			
			if num1 == 1:
				pb1.BackgroundImage = im1
			elif num1 == 2:
				pb1.BackgroundImage = im2
			elif num1 == 3:
				pb1.BackgroundImage = im3
			elif num1 == 4:
				pb1.BackgroundImage = im4
			elif num1 == 5:
				pb1.BackgroundImage = im5
				
			if num2 == 1:
				pb2.BackgroundImage = im1
			elif num2 == 2:
				pb2.BackgroundImage = im2
			elif num2 == 3:
				pb2.BackgroundImage = im3
			elif num2 == 4:
				pb2.BackgroundImage = im4
			elif num2 == 5:
				pb2.BackgroundImage = im5
				
			if num3 == 1:
				pb3.BackgroundImage = im1
			elif num3 == 2:
				pb3.BackgroundImage = im2
			elif num3 == 3:
				pb3.BackgroundImage = im3
			elif num3 == 4:
				pb3.BackgroundImage = im4
			elif num3 == 5:
				pb3.BackgroundImage = im5
			
			self._progressBar1.Increment(1)
			if self._progressBar1.Value == self._progressBar1.Maximum:
				self._timer1.Enabled = False
				self._pictureBox1.Visible = False
				self._button1.BackgroundImage = levOff
		pass